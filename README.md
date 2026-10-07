# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_09:13:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,235 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 09:13:09 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-10-07 09:13:05 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 09:10:39 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-07 09:09:44 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.068 |  |
| 2026-10-07 09:09:40 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:07:13 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-07 09:06:18 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.010 |  |
| 2026-10-07 09:06:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:06:02 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-10-07 09:05:49 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | -0.039 |  |
| 2026-10-07 09:05:38 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-10-07 09:05:29 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.047 |  |
| 2026-10-07 09:05:20 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-07 09:05:13 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:05:10 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 09:04:55 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.050 |  |
| 2026-10-07 09:04:31 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.096 |  |
| 2026-10-07 09:04:29 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:04:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-07 09:04:04 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-07 09:03:47 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 09:03:39 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-07 09:03:38 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-10-07 09:03:37 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:03:09 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.010 |  |
| 2026-10-07 09:03:07 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.029 |  |
| 2026-10-07 09:03:00 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-10-07 09:02:35 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:02:29 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.043 |  |
| 2026-10-07 09:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-10-07 09:02:21 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-07 09:02:09 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:01:58 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:01:45 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.049 |  |
| 2026-10-07 09:01:45 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.082 |  |
| 2026-10-07 09:01:33 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:01:28 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:01:23 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-07 08:50:11 | Panadugama (Nilwala Ganga) | 5.68 | 🟡 Alert | 2.470 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 08:50:11 | Panadugama (Nilwala Ganga) | 5.68 | 🟡 Alert | 2.470 | 🔺 Rising |
| 2026-10-07 09:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-10-07 09:01:23 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-07 09:04:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-07 09:07:13 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-07 09:05:20 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-07 09:04:04 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-07 09:02:21 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-07 09:13:05 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 09:03:47 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 09:05:10 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 09:10:39 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-07 09:01:28 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:01:33 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:03:37 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:02:35 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:01:58 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:06:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:02:09 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:04:29 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:05:13 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:09:40 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:03:00 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-10-07 09:03:39 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-07 09:03:09 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.010 |  |
| 2026-10-07 09:05:38 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-10-07 09:06:18 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.010 |  |
| 2026-10-07 09:03:38 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-10-07 09:06:02 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-10-07 09:13:09 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-10-07 09:03:07 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.029 |  |
| 2026-10-07 09:05:49 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | -0.039 |  |
| 2026-10-07 09:02:29 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.043 |  |
| 2026-10-07 09:05:29 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.047 |  |
| 2026-10-07 09:01:45 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.049 |  |
| 2026-10-07 09:04:55 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.050 |  |
| 2026-10-07 09:09:44 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.068 |  |
| 2026-10-07 09:01:45 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.082 |  |
| 2026-10-07 09:04:31 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)