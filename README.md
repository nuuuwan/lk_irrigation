# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_22:27:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,612 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 22:27:57 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | -0.014 |  |
| 2026-06-13 22:27:42 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.014 |  |
| 2026-06-13 22:07:55 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-06-13 22:07:53 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:07:48 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:07:43 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.028 |  |
| 2026-06-13 22:05:51 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.019 |  |
| 2026-06-13 22:05:44 | Magura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.069 |  |
| 2026-06-13 22:05:07 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-06-13 22:04:50 | Rathnapura (Kalu Ganga) | 4.69 | 🟢 Normal | -0.089 |  |
| 2026-06-13 22:04:31 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:04:17 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-13 22:03:48 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:03:46 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:03:37 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.040 |  |
| 2026-06-13 22:03:32 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-06-13 22:03:30 | Deraniyagala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 22:03:28 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:03:26 | Nawalapitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.039 |  |
| 2026-06-13 22:03:25 | Ellagawa (Kalu Ganga) | 8.61 | 🟢 Normal | -0.023 |  |
| 2026-06-13 22:03:01 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-06-13 22:02:18 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-13 22:02:12 | Hanwella (Kelani Ganga) | 3.89 | 🟢 Normal | -0.010 |  |
| 2026-06-13 22:02:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-13 22:02:10 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:02:01 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.011 |  |
| 2026-06-13 22:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.56 | 🟠 Minor Flood | 0.000 |  |
| 2026-06-13 22:01:51 | Baddegama (Gin Ganga) | 3.16 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:01:45 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:01:29 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:01:06 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-13 22:00:55 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:00:55 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 22:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.56 | 🟠 Minor Flood | 0.000 |  |
| 2026-06-13 22:03:01 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-06-13 22:02:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-13 18:01:49 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-13 22:01:06 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-13 22:04:17 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-13 22:02:18 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-13 22:03:30 | Deraniyagala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 22:07:48 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:02:10 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:03:28 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:01:44 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:00:55 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:03:46 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:01:51 | Baddegama (Gin Ganga) | 3.16 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:04:31 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:05:15 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:01:29 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:03:48 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:01:45 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:07:53 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:00:55 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-13 21:03:19 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-13 22:05:07 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-06-13 22:02:12 | Hanwella (Kelani Ganga) | 3.89 | 🟢 Normal | -0.010 |  |
| 2026-06-13 22:03:32 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-06-13 22:02:01 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.011 |  |
| 2026-06-13 22:27:42 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.014 |  |
| 2026-06-13 22:27:57 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | -0.014 |  |
| 2026-06-13 22:07:55 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-06-13 22:05:51 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.019 |  |
| 2026-06-13 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.021 |  |
| 2026-06-13 22:03:25 | Ellagawa (Kalu Ganga) | 8.61 | 🟢 Normal | -0.023 |  |
| 2026-06-13 22:07:43 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.028 |  |
| 2026-06-13 22:03:26 | Nawalapitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.039 |  |
| 2026-06-13 22:03:37 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.040 |  |
| 2026-06-13 18:05:47 | Galgamuwa (Mee Oya) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-06-13 22:05:44 | Magura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.069 |  |
| 2026-06-13 22:04:50 | Rathnapura (Kalu Ganga) | 4.69 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)