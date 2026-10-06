# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_02:30:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,966 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 02:30:15 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:18:49 | Panadugama (Nilwala Ganga) | 5.38 | 🟡 Alert | 0.250 | 🔺 Rising |
| 2026-10-07 02:16:38 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.050 |  |
| 2026-10-07 02:11:42 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-07 02:07:14 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-07 02:05:43 | Pitabeddara (Nilwala Ganga) | 2.98 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-07 02:05:19 | Hanwella (Kelani Ganga) | 2.79 | 🟢 Normal | -0.045 |  |
| 2026-10-07 02:05:05 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:04:58 | Thawalama (Gin Ganga) | 2.63 | 🟢 Normal | -0.050 |  |
| 2026-10-07 02:04:35 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-07 02:04:19 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:04:18 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.097 |  |
| 2026-10-07 02:04:06 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.495 |  |
| 2026-10-07 02:04:02 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-07 02:03:27 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-07 02:03:10 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:03:09 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:03:05 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-07 02:02:56 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.081 |  |
| 2026-10-07 02:02:50 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.035 |  |
| 2026-10-07 02:02:36 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.015 |  |
| 2026-10-07 02:02:22 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.049 |  |
| 2026-10-07 02:02:12 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:02:05 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.403 | 🔺 Rising |
| 2026-10-07 02:02:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:01:57 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 02:01:56 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:01:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.040 |  |
| 2026-10-07 02:01:12 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:01:05 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-10-07 01:57:19 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | 0.025 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 02:18:49 | Panadugama (Nilwala Ganga) | 5.38 | 🟡 Alert | 0.250 | 🔺 Rising |
| 2026-10-07 02:02:05 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.403 | 🔺 Rising |
| 2026-10-07 02:07:14 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-07 02:05:43 | Pitabeddara (Nilwala Ganga) | 2.98 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-07 02:04:02 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-07 02:03:05 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-07 02:04:35 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-07 01:06:36 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-07 02:11:42 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-07 01:57:19 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-07 02:01:57 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 01:02:48 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:02:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:01:56 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:01:59 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:05:05 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:01:12 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:02:12 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:01:05 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:03:10 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:04:19 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:28 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:30:15 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:03:09 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-07 02:03:27 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:01:43 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.011 |  |
| 2026-10-07 02:02:36 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.015 |  |
| 2026-10-07 02:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-10-07 02:02:50 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.035 |  |
| 2026-10-07 02:01:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.040 |  |
| 2026-10-07 02:05:19 | Hanwella (Kelani Ganga) | 2.79 | 🟢 Normal | -0.045 |  |
| 2026-10-07 02:02:22 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.049 |  |
| 2026-10-07 02:04:58 | Thawalama (Gin Ganga) | 2.63 | 🟢 Normal | -0.050 |  |
| 2026-10-07 02:16:38 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.050 |  |
| 2026-10-07 02:02:56 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.081 |  |
| 2026-10-07 01:02:08 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.082 |  |
| 2026-10-07 02:04:18 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.097 |  |
| 2026-10-07 02:04:06 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.495 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)