# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_13:04:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,769 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 13:04:28 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2025-12-13 13:04:25 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2025-12-13 13:04:07 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.029 |  |
| 2025-12-13 13:03:57 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:03:48 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.141 |  |
| 2025-12-13 13:03:46 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2025-12-13 13:03:40 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:03:27 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:03:09 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-13 13:03:06 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 13:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.069 |  |
| 2025-12-13 13:02:32 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.049 |  |
| 2025-12-13 13:02:20 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:02:17 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:02:06 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.020 |  |
| 2025-12-13 13:01:57 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-13 13:01:56 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2025-12-13 13:01:52 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2025-12-13 13:01:50 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-13 13:01:13 | Thanthirimale (Malwathu Oya) | 4.19 | 🟢 Normal | -0.010 |  |
| 2025-12-13 13:01:08 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.049 |  |
| 2025-12-13 13:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:01:03 | Horowpothana (Yan Oya) | 5.82 | 🟢 Normal | -0.020 |  |
| 2025-12-13 13:00:42 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:11:18 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:08:19 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:06:46 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:06:31 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:06:12 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 12:01:37 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-13 13:03:06 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 13:01:57 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-13 13:03:40 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:02:20 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:03:57 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:02:27 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:00:42 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:01:42 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:11:18 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:03:27 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:06:12 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:08:19 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:03:33 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:06:31 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:02:17 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-13 12:04:06 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-13 13:04:25 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2025-12-13 13:03:09 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-13 13:01:50 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-13 13:01:52 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2025-12-13 13:04:28 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2025-12-13 13:01:13 | Thanthirimale (Malwathu Oya) | 4.19 | 🟢 Normal | -0.010 |  |
| 2025-12-13 13:01:03 | Horowpothana (Yan Oya) | 5.82 | 🟢 Normal | -0.020 |  |
| 2025-12-13 13:02:06 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.020 |  |
| 2025-12-13 12:03:31 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2025-12-13 12:03:19 | Glencourse (Kelani Ganga) | 9.44 | 🟢 Normal | -0.021 |  |
| 2025-12-13 13:04:07 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.029 |  |
| 2025-12-13 13:03:46 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2025-12-13 12:01:32 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.040 |  |
| 2025-12-13 12:03:29 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.044 |  |
| 2025-12-13 13:02:32 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.049 |  |
| 2025-12-13 13:01:08 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.049 |  |
| 2025-12-13 12:03:18 | Weraganthota (Mahaweli Ganga) | -0.84 | 🟢 Normal | -0.061 |  |
| 2025-12-13 13:01:56 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2025-12-13 13:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.069 |  |
| 2025-12-13 12:03:12 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.138 |  |
| 2025-12-13 13:03:48 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)