# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_06:25:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,213 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 06:25:29 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.002 |  |
| 2026-10-06 06:18:04 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.028 |  |
| 2026-10-06 06:15:15 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:08:14 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-06 06:07:11 | Ellagawa (Kalu Ganga) | 6.14 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-06 06:07:10 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.045 |  |
| 2026-10-06 06:06:58 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-10-06 06:06:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:06:45 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.013 |  |
| 2026-10-06 06:06:17 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:04:45 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | -0.038 |  |
| 2026-10-06 06:04:37 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.057 |  |
| 2026-10-06 06:04:36 | Magura (Kalu Ganga) | 2.99 | 🟢 Normal | -0.129 |  |
| 2026-10-06 06:04:24 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.063 |  |
| 2026-10-06 06:04:17 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 06:04:10 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 06:04:08 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-06 06:03:39 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:03:15 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.191 |  |
| 2026-10-06 06:03:07 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.051 |  |
| 2026-10-06 06:03:05 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-06 06:03:03 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-06 06:02:51 | Glencourse (Kelani Ganga) | 12.11 | 🟢 Normal | -0.189 |  |
| 2026-10-06 06:02:44 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:02:35 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:02:29 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.080 |  |
| 2026-10-06 06:02:22 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-10-06 06:02:09 | Dunamale (Aththanagalu Oya) | 2.61 | 🟢 Normal | -0.020 |  |
| 2026-10-06 06:01:54 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-06 06:01:41 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:01:37 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.046 |  |
| 2026-10-06 06:01:07 | Hanwella (Kelani Ganga) | 4.32 | 🟢 Normal | -0.137 |  |
| 2026-10-06 06:01:03 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 06:00:47 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:00:45 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.049 |  |
| 2026-10-06 06:00:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-10-06 06:00:15 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.062 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 06:00:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-10-06 06:08:14 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-06 06:01:54 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-06 06:03:05 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-06 06:07:11 | Ellagawa (Kalu Ganga) | 6.14 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-06 06:03:03 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-06 06:04:08 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-06 06:01:03 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 06:04:17 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 06:04:10 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 06:02:44 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:01:37 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:15:15 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:03:39 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:06:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:02:35 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:00:47 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:03:21 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:01:41 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:06:17 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-06 06:25:29 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.002 |  |
| 2026-10-06 06:06:58 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-10-06 06:02:22 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-10-06 06:06:45 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.013 |  |
| 2026-10-06 06:02:09 | Dunamale (Aththanagalu Oya) | 2.61 | 🟢 Normal | -0.020 |  |
| 2026-10-06 06:18:04 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.028 |  |
| 2026-10-06 06:04:45 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | -0.038 |  |
| 2026-10-06 06:07:10 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.045 |  |
| 2026-10-06 06:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.046 |  |
| 2026-10-06 06:00:45 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.049 |  |
| 2026-10-06 06:03:07 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.051 |  |
| 2026-10-06 06:04:37 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.057 |  |
| 2026-10-06 06:00:15 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.062 |  |
| 2026-10-06 06:04:24 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.063 |  |
| 2026-10-06 06:02:29 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.080 |  |
| 2026-10-06 06:04:36 | Magura (Kalu Ganga) | 2.99 | 🟢 Normal | -0.129 |  |
| 2026-10-06 06:01:07 | Hanwella (Kelani Ganga) | 4.32 | 🟢 Normal | -0.137 |  |
| 2026-10-06 06:02:51 | Glencourse (Kelani Ganga) | 12.11 | 🟢 Normal | -0.189 |  |
| 2026-10-06 06:03:15 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.191 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)