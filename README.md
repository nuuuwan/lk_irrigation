# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_14:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **328,007 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 14:03:20 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | -0.109 |  |
| 2026-11-28 14:03:15 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 14:02:55 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-11-28 14:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | -0.020 |  |
| 2026-11-28 14:02:50 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.126 |  |
| 2026-11-28 14:02:48 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-28 14:02:32 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-28 14:02:19 | Ellagawa (Kalu Ganga) | 6.94 | 🟢 Normal | -0.059 |  |
| 2026-11-28 14:02:08 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 14:02:05 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.045 |  |
| 2026-11-28 14:01:59 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-11-28 14:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-28 14:01:45 | Moragaswewa (Deduru Oya) | 2.21 | 🟢 Normal | -0.021 |  |
| 2026-11-28 14:01:11 | Thanamalwila (Kirindi Oya) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-28 14:01:06 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 14:01:06 | Kuda Oya (Kirindi Oya) | 2.37 | 🟢 Normal | -0.011 |  |
| 2026-11-28 14:00:22 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:38:43 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 13:38:43 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.000 |  |
| 2026-11-28 12:08:47 | Moraketiya (Walawe Ganga) | 3.13 | 🟡 Alert | -0.018 |  |
| 2026-11-28 14:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | -0.020 |  |
| 2026-11-28 13:03:11 | Panadugama (Nilwala Ganga) | 5.25 | 🟡 Alert | -0.040 |  |
| 2026-11-28 13:05:05 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-28 13:01:37 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-28 14:03:15 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 13:08:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:03:25 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:03:54 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-28 14:00:22 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-28 14:02:08 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 14:01:06 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:14:13 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-11-28 13:06:17 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-11-28 14:02:32 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-28 13:03:07 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-11-28 14:01:59 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-11-28 14:02:48 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-28 14:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-28 14:01:06 | Kuda Oya (Kirindi Oya) | 2.37 | 🟢 Normal | -0.011 |  |
| 2026-11-28 13:06:54 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-11-28 13:02:48 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-11-28 13:08:48 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-28 14:01:11 | Thanamalwila (Kirindi Oya) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-28 14:01:45 | Moragaswewa (Deduru Oya) | 2.21 | 🟢 Normal | -0.021 |  |
| 2026-11-28 13:05:28 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.039 |  |
| 2026-11-28 14:02:05 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.045 |  |
| 2026-11-28 13:08:00 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.046 |  |
| 2026-11-28 14:02:55 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-11-28 14:02:19 | Ellagawa (Kalu Ganga) | 6.94 | 🟢 Normal | -0.059 |  |
| 2026-11-28 13:07:45 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | -0.062 |  |
| 2026-11-28 13:16:37 | Magura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.063 |  |
| 2026-11-28 13:11:20 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | -0.070 |  |
| 2026-11-28 13:07:48 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.080 |  |
| 2026-11-28 14:03:20 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | -0.109 |  |
| 2026-11-28 14:02:50 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.126 |  |
| 2026-11-28 13:01:45 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.145 |  |
| 2026-11-28 13:00:49 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.203 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)