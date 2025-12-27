# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_19:26:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,535 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 19:26:25 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.014 |  |
| 2025-12-27 19:23:09 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:19:51 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:19:39 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.008 |  |
| 2025-12-27 19:15:41 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:15:04 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2025-12-27 19:14:59 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.017 |  |
| 2025-12-27 19:14:29 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.016 |  |
| 2025-12-27 19:12:18 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-27 19:10:53 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:08:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.018 |  |
| 2025-12-27 19:07:33 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.059 |  |
| 2025-12-27 19:07:19 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:07:08 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.038 |  |
| 2025-12-27 19:07:07 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:07:04 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:06:57 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:06:15 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.045 |  |
| 2025-12-27 19:05:13 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 19:05:00 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:03:41 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:03:34 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:03:23 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:03:05 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.081 |  |
| 2025-12-27 19:03:04 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:03:01 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:02:59 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-27 19:02:46 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2025-12-27 19:02:35 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-27 19:02:17 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:02:01 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:01:49 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:01:45 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:01:14 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:01:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:01:00 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 19:00:41 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -0.011 |  |
| 2025-12-27 19:00:34 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 19:15:04 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2025-12-27 19:02:46 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2025-12-27 19:12:18 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-27 19:02:59 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-27 19:01:00 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 19:05:13 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 19:15:41 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:03:23 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:02:17 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:23:09 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:01:45 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:07:04 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:28 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:07:19 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:07:07 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:03:04 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:02:01 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:06:57 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:01:14 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:03:41 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:03:01 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:05:00 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:01:49 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:19:51 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:10:53 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:01:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:19:39 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.008 |  |
| 2025-12-27 18:01:19 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-27 19:00:34 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-27 19:02:35 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-27 19:00:41 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -0.011 |  |
| 2025-12-27 19:26:25 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.014 |  |
| 2025-12-27 19:14:29 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.016 |  |
| 2025-12-27 19:14:59 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.017 |  |
| 2025-12-27 19:08:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.018 |  |
| 2025-12-27 19:07:08 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.038 |  |
| 2025-12-27 19:06:15 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.045 |  |
| 2025-12-27 19:07:33 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.059 |  |
| 2025-12-27 19:03:05 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)