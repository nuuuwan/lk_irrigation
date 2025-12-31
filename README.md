# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_13:17:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,850 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 13:17:58 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:14:59 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-31 13:14:04 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -0.017 |  |
| 2025-12-31 13:10:55 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.055 |  |
| 2025-12-31 13:10:54 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 13:07:16 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 13:07:04 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:06:16 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-31 13:06:03 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-31 13:05:35 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:05:08 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:05:00 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:04:57 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.010 |  |
| 2025-12-31 13:03:56 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:03:50 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.029 |  |
| 2025-12-31 13:03:22 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.038 |  |
| 2025-12-31 13:03:16 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:03:14 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-31 13:03:00 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2025-12-31 13:02:48 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:02:42 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2025-12-31 13:02:39 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.053 |  |
| 2025-12-31 13:02:28 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:02:24 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:02:23 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-31 13:02:10 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:02:07 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-31 13:02:04 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:01:45 | Peradeniya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.011 |  |
| 2025-12-31 13:01:37 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-31 13:01:29 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:01:25 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-31 13:01:14 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:00:55 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:00:45 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:00:26 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2025-12-31 13:00:13 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:00:12 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 13:01:25 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-31 13:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-31 13:02:07 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-31 13:01:37 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-31 13:02:23 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-31 13:07:16 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 13:10:54 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 13:14:59 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-31 13:00:13 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:01:29 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:03:56 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:05:35 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:03:14 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:17:58 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 12:07:17 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:02:10 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:03:16 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:05:00 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:02:24 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:05:08 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:07:04 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:00:45 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:02:48 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:01:14 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:00:55 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:02:04 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:02:28 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 13:03:00 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2025-12-31 13:06:16 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-31 13:04:57 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.010 |  |
| 2025-12-31 13:06:03 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-31 13:01:45 | Peradeniya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.011 |  |
| 2025-12-31 13:00:26 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2025-12-31 13:14:04 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -0.017 |  |
| 2025-12-31 13:02:42 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2025-12-31 13:03:50 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.029 |  |
| 2025-12-31 13:03:22 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.038 |  |
| 2025-12-31 13:02:39 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.053 |  |
| 2025-12-31 13:10:55 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.055 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)