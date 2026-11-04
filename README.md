# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_21:13:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,947 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 21:13:45 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:10:32 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:08:30 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-04 21:08:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-04 21:07:52 | Thanamalwila (Kirindi Oya) | 2.38 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-04 21:07:51 | Urawa (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-04 21:06:44 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | -0.039 |  |
| 2026-11-04 21:06:13 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.048 |  |
| 2026-11-04 21:06:00 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-11-04 21:05:48 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-11-04 21:05:27 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:05:13 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.019 |  |
| 2026-11-04 21:05:00 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:05:00 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-11-04 21:04:56 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-11-04 21:04:48 | Magura (Kalu Ganga) | 2.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 21:04:37 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:04:25 | Badalgama (Maha Oya) | 3.46 | 🟢 Normal | -0.034 |  |
| 2026-11-04 21:03:52 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-11-04 21:03:38 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-11-04 21:03:36 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:03:23 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 21:03:05 | Holombuwa (Kelani Ganga) | 1.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-04 21:03:02 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-11-04 21:03:00 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.049 |  |
| 2026-11-04 21:02:56 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-04 21:02:52 | Moragaswewa (Deduru Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:02:37 | Kuda Oya (Kirindi Oya) | 3.85 | 🟢 Normal | 0.575 | 🔺 Rising |
| 2026-11-04 21:02:19 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-11-04 21:02:13 | Moragaswewa (Deduru Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:01:49 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:01:36 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-11-04 21:01:26 | Rathnapura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.065 |  |
| 2026-11-04 21:01:18 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:01:06 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:00:52 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:00:14 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-11-04 21:00:12 | Wellawaya (Kirindi Oya) | 2.70 | 🟢 Normal | 0.271 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 21:08:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-04 21:02:37 | Kuda Oya (Kirindi Oya) | 3.85 | 🟢 Normal | 0.575 | 🔺 Rising |
| 2026-11-04 21:07:52 | Thanamalwila (Kirindi Oya) | 2.38 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-04 21:00:12 | Wellawaya (Kirindi Oya) | 2.70 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-11-04 21:03:02 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-11-04 21:07:51 | Urawa (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-04 21:02:56 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-04 21:08:30 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-04 21:03:05 | Holombuwa (Kelani Ganga) | 1.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-04 21:04:48 | Magura (Kalu Ganga) | 2.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 21:03:23 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 21:05:27 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:02:52 | Moragaswewa (Deduru Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:00:52 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:13:45 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:10:32 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:01:18 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:05:00 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:01:49 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:01:06 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-04 21:05:48 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-11-04 21:06:00 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-11-04 21:04:56 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-11-04 21:02:19 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-11-04 21:01:36 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-11-04 21:00:14 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-11-04 21:03:38 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-11-04 21:05:13 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.019 |  |
| 2026-11-04 21:05:00 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-04 21:04:25 | Badalgama (Maha Oya) | 3.46 | 🟢 Normal | -0.034 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-04 21:06:44 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | -0.039 |  |
| 2026-11-04 21:03:52 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-11-04 21:06:13 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.048 |  |
| 2026-11-04 21:03:00 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.049 |  |
| 2026-11-04 21:01:26 | Rathnapura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.065 |  |
| 2026-11-04 20:04:05 | Ellagawa (Kalu Ganga) | 6.63 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)