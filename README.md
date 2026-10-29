# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_05:30:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,885 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 05:30:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.54 | 🟠 Minor Flood | -0.027 |  |
| 2026-10-29 05:29:36 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:26:22 | Panadugama (Nilwala Ganga) | 5.97 | 🟡 Alert | -0.023 |  |
| 2026-10-29 05:25:54 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:11:38 | Putupaula (Kalu Ganga) | 3.75 | 🟡 Alert | 0.000 |  |
| 2026-10-29 05:10:00 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.091 |  |
| 2026-10-29 05:09:09 | Hanwella (Kelani Ganga) | 3.99 | 🟢 Normal | -0.018 |  |
| 2026-10-29 05:09:04 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-10-29 05:07:41 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-10-29 05:07:29 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-29 05:07:24 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.081 |  |
| 2026-10-29 05:07:16 | Urawa (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.035 |  |
| 2026-10-29 05:06:34 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | -0.021 |  |
| 2026-10-29 05:06:31 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:06:05 | Pitabeddara (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-10-29 05:05:36 | Ellagawa (Kalu Ganga) | 10.20 | 🟡 Alert | -0.029 |  |
| 2026-10-29 05:05:15 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:05:08 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.041 |  |
| 2026-10-29 05:04:37 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.058 |  |
| 2026-10-29 05:04:21 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-29 05:03:55 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-29 05:03:27 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-29 05:03:24 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-29 05:03:15 | Moragaswewa (Deduru Oya) | 1.72 | 🟢 Normal | -0.108 |  |
| 2026-10-29 05:03:08 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:02:45 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:02:38 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.051 |  |
| 2026-10-29 05:02:36 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:02:35 | Rathnapura (Kalu Ganga) | 5.18 | 🟢 Normal | -0.097 |  |
| 2026-10-29 05:02:19 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-10-29 05:01:20 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-10-29 05:01:01 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-29 05:00:52 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:00:12 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 05:00:12 | Magura (Kalu Ganga) | 3.85 | 🟢 Normal | -0.074 |  |
| 2026-10-29 04:55:53 | Putupaula (Kalu Ganga) | 3.75 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 05:03:27 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-29 05:07:29 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-29 05:30:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.54 | 🟠 Minor Flood | -0.027 |  |
| 2026-10-29 05:11:38 | Putupaula (Kalu Ganga) | 3.75 | 🟡 Alert | 0.000 |  |
| 2026-10-29 05:26:22 | Panadugama (Nilwala Ganga) | 5.97 | 🟡 Alert | -0.023 |  |
| 2026-10-29 05:05:36 | Ellagawa (Kalu Ganga) | 10.20 | 🟡 Alert | -0.029 |  |
| 2026-10-28 18:01:08 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-29 05:01:01 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-29 05:00:12 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 18:08:56 | Galgamuwa (Mee Oya) | 2.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-29 05:00:52 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:02:09 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:02:45 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:02:36 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:03:08 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:05:15 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:25:54 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:06:31 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:29:36 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-29 05:04:21 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-29 05:03:55 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-29 05:03:24 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-29 05:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-10-29 05:09:09 | Hanwella (Kelani Ganga) | 3.99 | 🟢 Normal | -0.018 |  |
| 2026-10-29 05:07:41 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-10-29 05:09:04 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-10-29 05:06:05 | Pitabeddara (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-10-29 05:06:34 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | -0.021 |  |
| 2026-10-29 05:01:20 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-10-29 05:07:16 | Urawa (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.035 |  |
| 2026-10-29 05:05:08 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.041 |  |
| 2026-10-29 05:02:38 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.051 |  |
| 2026-10-29 05:04:37 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.058 |  |
| 2026-10-28 18:02:07 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-10-29 05:00:12 | Magura (Kalu Ganga) | 3.85 | 🟢 Normal | -0.074 |  |
| 2026-10-29 05:07:24 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.081 |  |
| 2026-10-29 05:10:00 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.091 |  |
| 2026-10-29 05:02:35 | Rathnapura (Kalu Ganga) | 5.18 | 🟢 Normal | -0.097 |  |
| 2026-10-29 05:03:15 | Moragaswewa (Deduru Oya) | 1.72 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)