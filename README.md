# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_16:03:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,396 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 16:03:38 | Urawa (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.144 |  |
| 2026-10-28 16:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 16:03:31 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-10-28 16:03:31 | Ellagawa (Kalu Ganga) | 10.41 | 🟡 Alert | -0.011 |  |
| 2026-10-28 16:03:22 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:03:06 | Hanwella (Kelani Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2026-10-28 16:02:51 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.049 |  |
| 2026-10-28 16:02:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-28 16:02:13 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-28 16:02:10 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-28 16:02:03 | Pitabeddara (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-10-28 16:01:53 | Dunamale (Aththanagalu Oya) | 3.37 | 🟡 Alert | -0.104 |  |
| 2026-10-28 16:01:38 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-10-28 16:01:33 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:01:26 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:01:20 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:01:10 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.052 |  |
| 2026-10-28 16:00:23 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-28 15:30:01 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 15:06:34 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 15:08:41 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 15:06:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.72 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 15:04:44 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-10-28 15:02:33 | Putupaula (Kalu Ganga) | 3.68 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-28 15:06:28 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | -0.009 |  |
| 2026-10-28 16:03:31 | Ellagawa (Kalu Ganga) | 10.41 | 🟡 Alert | -0.011 |  |
| 2026-10-28 15:04:20 | Rathnapura (Kalu Ganga) | 6.09 | 🟡 Alert | -0.059 |  |
| 2026-10-28 16:01:53 | Dunamale (Aththanagalu Oya) | 3.37 | 🟡 Alert | -0.104 |  |
| 2026-10-28 16:02:03 | Pitabeddara (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-10-28 15:03:04 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-10-28 15:07:32 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-28 15:04:17 | Glencourse (Kelani Ganga) | 11.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-28 15:02:41 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-28 15:02:25 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 16:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 16:00:23 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-28 15:03:20 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-10-28 15:04:14 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:01:33 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:01:20 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:03:22 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:01:26 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:02:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-28 16:02:10 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-28 16:03:06 | Hanwella (Kelani Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2026-10-28 15:03:31 | Thawalama (Gin Ganga) | 3.35 | 🟢 Normal | -0.011 |  |
| 2026-10-28 16:02:13 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-28 15:03:04 | Moragaswewa (Deduru Oya) | 3.06 | 🟢 Normal | -0.020 |  |
| 2026-10-28 15:30:01 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-10-28 15:01:23 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.023 |  |
| 2026-10-28 15:02:06 | Galgamuwa (Mee Oya) | 2.33 | 🟢 Normal | -0.026 |  |
| 2026-10-28 15:04:36 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-10-28 16:03:31 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-10-28 16:01:38 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-10-28 15:02:32 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.040 |  |
| 2026-10-28 16:02:51 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.049 |  |
| 2026-10-28 16:01:10 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.052 |  |
| 2026-10-28 16:03:38 | Urawa (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)