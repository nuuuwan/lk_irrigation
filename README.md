# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_15:02:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,298 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 15:02:53 | Putupaula (Kalu Ganga) | 1.83 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-08 15:02:51 | Badalgama (Maha Oya) | 3.74 | 🟢 Normal | -0.050 |  |
| 2026-11-08 15:02:48 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-08 15:02:48 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | -0.080 |  |
| 2026-11-08 15:02:33 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | -0.040 |  |
| 2026-11-08 15:02:29 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | -0.021 |  |
| 2026-11-08 15:02:28 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-08 15:02:27 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-08 15:02:10 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.022 |  |
| 2026-11-08 15:02:09 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-11-08 15:02:06 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.099 |  |
| 2026-11-08 15:02:05 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-08 15:01:11 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 15:01:08 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 15:00:56 | Manampitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-08 15:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-11-08 14:34:47 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -18.000 |  |
| 2026-11-08 14:34:45 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -18.000 |  |
| 2026-11-08 14:25:19 | Dunamale (Aththanagalu Oya) | 3.44 | 🟡 Alert | -0.030 |  |
| 2026-11-08 14:18:58 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.029 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 15:02:05 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-08 14:02:56 | Moraketiya (Walawe Ganga) | 3.19 | 🟡 Alert | -0.020 |  |
| 2026-11-08 14:06:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.41 | 🟡 Alert | -0.020 |  |
| 2026-11-08 14:25:19 | Dunamale (Aththanagalu Oya) | 3.44 | 🟡 Alert | -0.030 |  |
| 2026-11-08 14:01:38 | Panadugama (Nilwala Ganga) | 5.77 | 🟡 Alert | -0.061 |  |
| 2026-11-08 15:02:09 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-11-08 15:02:53 | Putupaula (Kalu Ganga) | 1.83 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-08 15:02:28 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-08 14:05:57 | Moragaswewa (Deduru Oya) | 3.15 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-08 15:00:56 | Manampitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-08 14:03:39 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 15:01:08 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 14:01:28 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-08 15:01:11 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 15:02:48 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-08 14:11:45 | Baddegama (Gin Ganga) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-11-08 14:02:37 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 14:04:11 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-08 15:02:27 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-08 14:12:14 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-08 14:01:25 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-08 14:02:27 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-11-08 14:04:17 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-08 14:06:39 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.019 |  |
| 2026-11-08 14:02:06 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-11-08 14:02:24 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-11-08 15:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-11-08 15:02:29 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | -0.021 |  |
| 2026-11-08 15:02:10 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.022 |  |
| 2026-11-08 15:02:33 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | -0.040 |  |
| 2026-11-08 14:03:15 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | -0.043 |  |
| 2026-11-08 15:02:51 | Badalgama (Maha Oya) | 3.74 | 🟢 Normal | -0.050 |  |
| 2026-11-08 15:02:48 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | -0.080 |  |
| 2026-11-08 15:02:06 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.099 |  |
| 2026-11-08 14:07:13 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | -0.100 |  |
| 2026-11-08 14:10:26 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | -0.146 |  |
| 2026-11-08 14:05:31 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.151 |  |
| 2026-11-08 13:55:05 | Magura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.210 |  |
| 2026-11-08 14:34:47 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)