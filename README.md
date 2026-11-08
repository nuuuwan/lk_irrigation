# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_08:03:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,024 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 08:03:31 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.029 |  |
| 2026-11-08 08:03:16 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.021 |  |
| 2026-11-08 08:03:08 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.136 |  |
| 2026-11-08 08:03:07 | Panadugama (Nilwala Ganga) | 6.06 | 🟠 Minor Flood | -0.023 |  |
| 2026-11-08 08:03:05 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.022 |  |
| 2026-11-08 08:02:45 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.050 |  |
| 2026-11-08 08:02:39 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | -0.073 |  |
| 2026-11-08 08:02:33 | Peradeniya (Mahaweli Ganga) | 3.16 | 🟢 Normal | -0.021 |  |
| 2026-11-08 08:02:29 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-11-08 08:02:27 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.101 |  |
| 2026-11-08 08:02:26 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-11-08 08:02:15 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | -0.081 |  |
| 2026-11-08 08:02:09 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-08 08:02:05 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-08 08:01:43 | Thanamalwila (Kirindi Oya) | 2.06 | 🟢 Normal | -0.100 |  |
| 2026-11-08 08:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-08 08:01:13 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-08 08:00:56 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.017 |  |
| 2026-11-08 08:00:32 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 08:03:07 | Panadugama (Nilwala Ganga) | 6.06 | 🟠 Minor Flood | -0.023 |  |
| 2026-11-08 07:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.35 | 🟡 Alert | 0.203 | 🔺 Rising |
| 2026-11-08 07:04:25 | Dunamale (Aththanagalu Oya) | 3.72 | 🟡 Alert | -0.030 |  |
| 2026-11-08 07:00:59 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.042 |  |
| 2026-11-08 07:05:37 | Moraketiya (Walawe Ganga) | 3.43 | 🟡 Alert | -0.259 |  |
| 2026-11-08 07:00:28 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-11-08 08:02:09 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-08 07:16:44 | Moragaswewa (Deduru Oya) | 2.40 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-11-08 07:02:44 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-08 07:12:15 | Baddegama (Gin Ganga) | 2.94 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-08 07:04:33 | Ellagawa (Kalu Ganga) | 7.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-08 07:00:20 | Thalgahagoda (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 08:02:05 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-08 07:08:11 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-08 08:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-08 08:01:13 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-08 07:10:14 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-08 07:05:11 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 07:04:35 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-11-08 08:00:32 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-11-08 08:02:29 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-11-08 08:00:56 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.017 |  |
| 2026-11-08 08:03:16 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.021 |  |
| 2026-11-08 08:02:33 | Peradeniya (Mahaweli Ganga) | 3.16 | 🟢 Normal | -0.021 |  |
| 2026-11-08 08:03:05 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.022 |  |
| 2026-11-08 07:05:22 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | -0.029 |  |
| 2026-11-08 08:03:31 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.029 |  |
| 2026-11-08 08:02:26 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-11-08 08:02:45 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.050 |  |
| 2026-11-08 07:04:32 | Thawalama (Gin Ganga) | 2.97 | 🟢 Normal | -0.056 |  |
| 2026-11-08 07:01:48 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.065 |  |
| 2026-11-08 08:02:39 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | -0.073 |  |
| 2026-11-08 08:02:15 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | -0.081 |  |
| 2026-11-08 08:01:43 | Thanamalwila (Kirindi Oya) | 2.06 | 🟢 Normal | -0.100 |  |
| 2026-11-08 08:02:27 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.101 |  |
| 2026-11-08 07:06:53 | Urawa (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.122 |  |
| 2026-11-08 07:00:56 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.132 |  |
| 2026-11-08 08:03:08 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.136 |  |
| 2026-11-08 07:05:59 | Kuda Oya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.264 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)