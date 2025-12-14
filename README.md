# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_19:16:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,933 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 19:16:16 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-14 19:13:32 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-14 19:13:05 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-14 19:12:51 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.017 |  |
| 2025-12-14 19:11:21 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-14 19:09:28 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-14 19:07:28 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 19:07:18 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-14 19:06:50 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -0.142 |  |
| 2025-12-14 19:06:35 | Manampitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.019 |  |
| 2025-12-14 19:06:00 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-14 19:05:29 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.030 |  |
| 2025-12-14 19:05:12 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-14 19:05:05 | Glencourse (Kelani Ganga) | 9.17 | 🟢 Normal | -0.029 |  |
| 2025-12-14 19:04:32 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2025-12-14 19:04:12 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.038 |  |
| 2025-12-14 19:04:11 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-14 19:03:58 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-14 19:02:57 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-14 19:02:56 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-14 19:02:56 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2025-12-14 19:02:48 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2025-12-14 19:02:23 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2025-12-14 19:02:14 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-14 19:02:12 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2025-12-14 19:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 19:01:47 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 19:01:33 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-14 19:01:24 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-14 19:01:23 | Horowpothana (Yan Oya) | 4.25 | 🟢 Normal | -0.010 |  |
| 2025-12-14 19:00:48 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-14 19:00:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.041 |  |
| 2025-12-14 19:00:17 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 19:02:12 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2025-12-14 19:02:56 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2025-12-14 19:06:00 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-14 19:04:11 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-14 19:02:57 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-14 19:16:16 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-14 18:05:46 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-14 19:11:21 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-14 19:01:33 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-14 19:07:18 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-14 19:13:05 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-14 19:02:56 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-14 19:13:32 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-14 19:09:28 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-14 19:00:48 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-14 19:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 19:01:24 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:09 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:08:28 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2025-12-14 19:01:47 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 19:02:14 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-14 19:07:28 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:24 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-14 19:00:17 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:04:06 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2025-12-14 19:03:58 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:05:18 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-14 19:05:12 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-14 19:01:23 | Horowpothana (Yan Oya) | 4.25 | 🟢 Normal | -0.010 |  |
| 2025-12-14 19:12:51 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.017 |  |
| 2025-12-14 19:06:35 | Manampitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.019 |  |
| 2025-12-14 19:02:23 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2025-12-14 19:02:48 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2025-12-14 19:05:05 | Glencourse (Kelani Ganga) | 9.17 | 🟢 Normal | -0.029 |  |
| 2025-12-14 19:05:29 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.030 |  |
| 2025-12-14 19:04:12 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.038 |  |
| 2025-12-14 19:00:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.041 |  |
| 2025-12-14 19:04:32 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2025-12-14 19:06:50 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)