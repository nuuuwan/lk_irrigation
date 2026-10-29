# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_21:02:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,497 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Putupaula — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 21:02:53 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.078 |  |
| 2026-10-29 21:02:50 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | -0.011 |  |
| 2026-10-29 21:02:49 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-29 21:02:48 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:46 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-29 21:02:39 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-10-29 21:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:26 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:25 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-29 21:02:24 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:15 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:12 | Hanwella (Kelani Ganga) | 3.32 | 🟢 Normal | -0.010 |  |
| 2026-10-29 21:02:11 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:04 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.011 |  |
| 2026-10-29 21:01:59 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | -0.059 |  |
| 2026-10-29 21:01:47 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-29 21:01:33 | Putupaula (Kalu Ganga) | 3.62 | 🟡 Alert | -0.011 |  |
| 2026-10-29 21:01:24 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-10-29 21:01:19 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-10-29 21:00:25 | Magura (Kalu Ganga) | 3.12 | 🟢 Normal | -0.043 |  |
| 2026-10-29 20:47:27 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-29 20:25:34 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 20:06:15 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 21:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | -0.059 |  |
| 2026-10-29 20:05:01 | Panadugama (Nilwala Ganga) | 5.74 | 🟡 Alert | 0.000 |  |
| 2026-10-29 21:01:33 | Putupaula (Kalu Ganga) | 3.62 | 🟡 Alert | -0.011 |  |
| 2026-10-29 20:08:33 | Baddegama (Gin Ganga) | 3.90 | 🟡 Alert | -0.029 |  |
| 2026-10-29 18:05:01 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-29 21:02:49 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-29 21:02:25 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-29 21:02:46 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-29 20:00:13 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 21:02:26 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:01:59 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-29 20:09:06 | Pitabeddara (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-29 20:03:53 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 20:02:36 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:48 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:24 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:15 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:11 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-29 20:05:21 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:39 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-10-29 18:06:21 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-10-29 20:06:01 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-29 21:02:12 | Hanwella (Kelani Ganga) | 3.32 | 🟢 Normal | -0.010 |  |
| 2026-10-29 20:04:00 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-29 21:01:47 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-29 21:02:04 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.011 |  |
| 2026-10-29 21:02:50 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | -0.011 |  |
| 2026-10-29 21:01:19 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-10-29 20:05:11 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.021 |  |
| 2026-10-29 21:01:24 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-10-29 20:01:39 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-10-29 20:07:38 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.032 |  |
| 2026-10-29 21:00:25 | Magura (Kalu Ganga) | 3.12 | 🟢 Normal | -0.043 |  |
| 2026-10-29 20:01:31 | Rathnapura (Kalu Ganga) | 4.29 | 🟢 Normal | -0.052 |  |
| 2026-10-29 18:01:49 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.059 |  |
| 2026-10-29 21:02:53 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.078 |  |
| 2026-10-29 20:04:37 | Ellagawa (Kalu Ganga) | 9.62 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)