# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_18:19:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,694 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 18:19:25 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-16 18:11:46 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:10:17 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:08:47 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 18:07:55 | Pitabeddara (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-16 18:07:09 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-16 18:07:03 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-16 18:05:39 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | -0.058 |  |
| 2026-10-16 18:05:18 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-10-16 18:05:05 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-10-16 18:05:04 | Panadugama (Nilwala Ganga) | 6.44 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-16 18:04:59 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:04:27 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | -0.042 |  |
| 2026-10-16 18:03:54 | Moragaswewa (Deduru Oya) | 2.24 | 🟢 Normal | -0.051 |  |
| 2026-10-16 18:03:18 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-10-16 18:02:59 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:02:58 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-16 18:02:58 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:02:54 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-16 18:02:46 | Thawalama (Gin Ganga) | 3.36 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-16 18:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | -0.010 |  |
| 2026-10-16 18:02:38 | Galgamuwa (Mee Oya) | 2.02 | 🟢 Normal | -0.023 |  |
| 2026-10-16 18:02:35 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-10-16 18:02:25 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.021 |  |
| 2026-10-16 18:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-10-16 18:02:13 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-10-16 18:02:11 | Baddegama (Gin Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:02:06 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-16 18:01:58 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 18:01:55 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:01:52 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-10-16 18:01:35 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-16 18:01:14 | Putupaula (Kalu Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:01:05 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 18:00:38 | Magura (Kalu Ganga) | 3.34 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-10-16 18:00:28 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | 0.896 | 🔺 Rising |
| 2026-10-16 18:00:22 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-16 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-16 18:00:08 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.014 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 18:08:47 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 18:05:04 | Panadugama (Nilwala Ganga) | 6.44 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-16 18:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | -0.010 |  |
| 2026-10-16 18:00:28 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | 0.896 | 🔺 Rising |
| 2026-10-16 18:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-10-16 18:05:18 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-10-16 18:02:46 | Thawalama (Gin Ganga) | 3.36 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-16 18:03:18 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-10-16 18:00:38 | Magura (Kalu Ganga) | 3.34 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-10-16 18:19:25 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-16 18:01:35 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-16 18:00:22 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-16 18:02:06 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-16 18:07:55 | Pitabeddara (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-16 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-16 18:02:58 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-16 18:07:03 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-16 18:00:08 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-16 18:01:05 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 18:01:58 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 18:02:59 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:02:58 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:02:11 | Baddegama (Gin Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:11:46 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:10:17 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:01:14 | Putupaula (Kalu Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:04:59 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:01:55 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:07:09 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-16 18:02:13 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-10-16 18:02:54 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-16 18:05:05 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-10-16 18:02:35 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-10-16 18:02:25 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.021 |  |
| 2026-10-16 18:02:38 | Galgamuwa (Mee Oya) | 2.02 | 🟢 Normal | -0.023 |  |
| 2026-10-16 18:01:52 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-10-16 18:04:27 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | -0.042 |  |
| 2026-10-16 18:03:54 | Moragaswewa (Deduru Oya) | 2.24 | 🟢 Normal | -0.051 |  |
| 2026-10-16 18:05:39 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)