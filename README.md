# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_14:07:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,813 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 14:07:38 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.026 |  |
| 2025-12-13 14:05:53 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-13 14:05:28 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | -0.009 |  |
| 2025-12-13 14:04:55 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-13 14:03:35 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:03:25 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | -0.030 |  |
| 2025-12-13 14:03:13 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:03:08 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2025-12-13 14:02:59 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 14:02:59 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.030 |  |
| 2025-12-13 14:02:55 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:02:53 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.114 |  |
| 2025-12-13 14:02:49 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-13 14:02:36 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -1.500 |  |
| 2025-12-13 14:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.31 | 🟢 Normal | -0.091 |  |
| 2025-12-13 14:02:17 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:02:16 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:02:16 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:02:12 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2025-12-13 14:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -1.500 |  |
| 2025-12-13 14:02:08 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.011 |  |
| 2025-12-13 14:01:56 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-13 14:01:49 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.012 |  |
| 2025-12-13 14:01:46 | Horowpothana (Yan Oya) | 5.76 | 🟢 Normal | -0.059 |  |
| 2025-12-13 14:01:46 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.061 |  |
| 2025-12-13 14:01:35 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.021 |  |
| 2025-12-13 14:01:30 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.025 |  |
| 2025-12-13 14:01:09 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.032 |  |
| 2025-12-13 14:00:09 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-13 13:25:52 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:20:41 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.026 |  |
| 2025-12-13 13:17:45 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.016 |  |
| 2025-12-13 13:12:42 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.012 |  |
| 2025-12-13 13:10:39 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:10:20 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.114 |  |
| 2025-12-13 13:09:39 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 14:05:53 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-13 14:02:59 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 13:01:57 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-13 14:02:16 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:03:35 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:03:13 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:02:17 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:00:42 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:02:55 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:02:16 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:10:39 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:05:33 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:02:36 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-13 14:05:28 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | -0.009 |  |
| 2025-12-13 14:02:49 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-13 14:02:12 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2025-12-13 14:00:09 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-13 14:04:55 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-13 14:01:56 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-13 13:07:32 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2025-12-13 14:02:08 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.011 |  |
| 2025-12-13 14:01:49 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.012 |  |
| 2025-12-13 13:17:45 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.016 |  |
| 2025-12-13 13:05:49 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2025-12-13 13:02:06 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.020 |  |
| 2025-12-13 14:01:35 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.021 |  |
| 2025-12-13 14:01:30 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.025 |  |
| 2025-12-13 14:07:38 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.026 |  |
| 2025-12-13 14:03:08 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2025-12-13 14:03:25 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | -0.030 |  |
| 2025-12-13 14:02:59 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.030 |  |
| 2025-12-13 14:01:09 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.032 |  |
| 2025-12-13 13:01:08 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.049 |  |
| 2025-12-13 14:01:46 | Horowpothana (Yan Oya) | 5.76 | 🟢 Normal | -0.059 |  |
| 2025-12-13 14:01:46 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.061 |  |
| 2025-12-13 14:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.31 | 🟢 Normal | -0.091 |  |
| 2025-12-13 13:06:43 | Weraganthota (Mahaweli Ganga) | -0.95 | 🟢 Normal | -0.104 |  |
| 2025-12-13 14:02:53 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.114 |  |
| 2025-12-13 14:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -1.500 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)