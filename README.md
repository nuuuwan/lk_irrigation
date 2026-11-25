# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_22:03:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,661 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 22:03:03 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 22:02:56 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-11-25 22:02:43 | Giriulla (Maha Oya) | 2.72 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-25 22:02:35 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.238 |  |
| 2026-11-25 22:02:28 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-11-25 22:02:28 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-25 22:02:24 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-25 22:02:20 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-25 22:02:20 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | 0.123 | 🔺 Rising |
| 2026-11-25 22:02:12 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 22:02:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-11-25 22:02:04 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-25 22:01:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-25 22:01:04 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-25 22:00:49 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | -0.032 |  |
| 2026-11-25 22:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-11-25 22:00:30 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-25 22:00:14 | Peradeniya (Mahaweli Ganga) | 5.26 | 🟡 Alert | -0.241 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 22:02:20 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | 0.123 | 🔺 Rising |
| 2026-11-25 22:00:14 | Peradeniya (Mahaweli Ganga) | 5.26 | 🟡 Alert | -0.241 |  |
| 2026-11-25 20:05:34 | Magura (Kalu Ganga) | 3.40 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-11-25 21:04:48 | Glencourse (Kelani Ganga) | 11.56 | 🟢 Normal | 0.428 | 🔺 Rising |
| 2026-11-25 22:02:56 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-11-25 22:02:43 | Giriulla (Maha Oya) | 2.72 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-25 18:02:46 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-25 22:02:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-11-25 22:02:04 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-25 22:02:28 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-25 21:03:50 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-25 18:02:35 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-25 18:00:42 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-25 21:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.79 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 22:02:20 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-25 22:03:03 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 22:02:12 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 22:01:04 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-25 22:01:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-25 21:05:27 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-11-25 22:02:24 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-25 22:00:30 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-25 21:02:22 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.011 |  |
| 2026-11-25 21:08:52 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.012 |  |
| 2026-11-25 21:03:18 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-11-25 21:04:28 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-11-25 22:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 21:02:05 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.022 |  |
| 2026-11-25 21:03:35 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.029 |  |
| 2026-11-25 22:02:28 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-11-25 21:06:53 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | -0.032 |  |
| 2026-11-25 22:00:49 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | -0.032 |  |
| 2026-11-25 21:04:19 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.050 |  |
| 2026-11-25 21:03:02 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.060 |  |
| 2026-11-25 21:12:53 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.061 |  |
| 2026-11-25 21:05:31 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.065 |  |
| 2026-11-25 21:05:47 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | -0.200 |  |
| 2026-11-25 22:02:35 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.238 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)