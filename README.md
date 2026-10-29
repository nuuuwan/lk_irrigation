# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_22:03:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,528 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Putupaula — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 22:03:50 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-10-29 22:03:34 | Glencourse (Kelani Ganga) | 11.01 | 🟢 Normal | -0.010 |  |
| 2026-10-29 22:03:27 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.040 |  |
| 2026-10-29 22:03:00 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-29 22:02:48 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-29 22:02:34 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-29 22:02:17 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.030 |  |
| 2026-10-29 22:02:15 | Ellagawa (Kalu Ganga) | 9.55 | 🟢 Normal | -0.044 |  |
| 2026-10-29 22:02:12 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.020 |  |
| 2026-10-29 22:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-29 22:01:32 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.072 |  |
| 2026-10-29 22:01:29 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-10-29 22:01:14 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-10-29 22:01:13 | Panadugama (Nilwala Ganga) | 5.74 | 🟡 Alert | 0.000 |  |
| 2026-10-29 22:00:38 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-29 22:00:16 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-29 21:25:11 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 21:03:31 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 21:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | -0.059 |  |
| 2026-10-29 22:01:13 | Panadugama (Nilwala Ganga) | 5.74 | 🟡 Alert | 0.000 |  |
| 2026-10-29 21:01:33 | Putupaula (Kalu Ganga) | 3.62 | 🟡 Alert | -0.011 |  |
| 2026-10-29 21:08:28 | Baddegama (Gin Ganga) | 3.87 | 🟡 Alert | -0.030 |  |
| 2026-10-29 18:05:01 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-29 22:00:38 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-29 21:06:48 | Pitabeddara (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-29 22:00:16 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-29 22:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:01:59 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:10:30 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:25:11 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:48 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 22:02:34 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:05:40 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-29 22:02:48 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:15 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:02:11 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-29 21:06:03 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-29 22:03:00 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-29 18:06:21 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-10-29 22:03:34 | Glencourse (Kelani Ganga) | 11.01 | 🟢 Normal | -0.010 |  |
| 2026-10-29 21:01:47 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-29 21:07:10 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.019 |  |
| 2026-10-29 22:03:50 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-10-29 22:01:29 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-10-29 22:02:12 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.020 |  |
| 2026-10-29 21:01:19 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-10-29 22:01:14 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-10-29 21:05:22 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.021 |  |
| 2026-10-29 21:06:51 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.028 |  |
| 2026-10-29 22:02:17 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.030 |  |
| 2026-10-29 22:03:27 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.040 |  |
| 2026-10-29 21:00:25 | Magura (Kalu Ganga) | 3.12 | 🟢 Normal | -0.043 |  |
| 2026-10-29 22:02:15 | Ellagawa (Kalu Ganga) | 9.55 | 🟢 Normal | -0.044 |  |
| 2026-10-29 18:01:49 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.059 |  |
| 2026-10-29 22:01:32 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.072 |  |
| 2026-10-29 21:07:20 | Rathnapura (Kalu Ganga) | 4.21 | 🟢 Normal | -0.073 |  |

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)