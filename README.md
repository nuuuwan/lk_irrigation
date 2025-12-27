# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_18:11:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,496 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 18:11:06 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:10:56 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:06:08 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:05:43 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.033 |  |
| 2025-12-27 18:05:28 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.043 |  |
| 2025-12-27 18:05:17 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:05:09 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-27 18:05:08 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-27 18:04:53 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-27 18:04:42 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.061 |  |
| 2025-12-27 18:04:36 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2025-12-27 18:04:31 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:04:30 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:04:14 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2025-12-27 18:04:13 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:03:45 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.079 |  |
| 2025-12-27 18:03:28 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:21 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:14 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:03 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:02:39 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:02:38 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:02:31 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:02:22 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:02:20 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.03 | 🟢 Normal | -0.030 |  |
| 2025-12-27 18:02:11 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-27 18:01:57 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:01:41 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-27 18:01:19 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:01:18 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 18:01:14 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:01:11 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:01:07 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-27 18:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:00:30 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:00:24 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:00:12 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-27 17:55:51 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:23:19 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.043 |  |
| 2025-12-27 17:23:16 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:18:03 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 18:04:36 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2025-12-27 18:00:12 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-27 18:01:07 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-27 18:01:41 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-27 18:05:09 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-27 18:05:08 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-27 18:02:11 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-27 18:01:18 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 18:04:53 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-27 17:01:53 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:02:22 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:02:39 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:28 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:18:03 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:00:30 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:00:24 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:03 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:14 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:21 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:11:06 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:04:31 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:06:08 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:01:57 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:01:14 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:04:30 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:01:19 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:01:11 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:02:38 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:02:20 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:04:13 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:02:31 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:04:14 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2025-12-27 17:01:02 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2025-12-27 18:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.03 | 🟢 Normal | -0.030 |  |
| 2025-12-27 18:05:43 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.033 |  |
| 2025-12-27 18:05:28 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.043 |  |
| 2025-12-27 18:04:42 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.061 |  |
| 2025-12-27 18:03:45 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)