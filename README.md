# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_02:29:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,067 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 02:29:03 | Magura (Kalu Ganga) | 3.22 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-06 02:24:03 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:20:24 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-06 02:20:02 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-06 02:16:56 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-06 02:13:23 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.043 |  |
| 2026-10-06 02:12:43 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-10-06 02:12:24 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.026 |  |
| 2026-10-06 02:10:58 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-06 02:08:09 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.098 |  |
| 2026-10-06 02:06:38 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-10-06 02:06:13 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-06 02:05:55 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-06 02:05:22 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-06 02:05:06 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:03:42 | Thawalama (Gin Ganga) | 2.91 | 🟢 Normal | -0.136 |  |
| 2026-10-06 02:03:36 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-06 02:02:55 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:02:38 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 02:02:38 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-06 02:02:30 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:02:28 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:02:25 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:02:19 | Peradeniya (Mahaweli Ganga) | 3.49 | 🟢 Normal | -0.117 |  |
| 2026-10-06 02:01:51 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-06 02:01:43 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:01:34 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.032 |  |
| 2026-10-06 02:00:32 | Glencourse (Kelani Ganga) | 13.00 | 🟢 Normal | -0.062 |  |
| 2026-10-06 02:00:15 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 02:00:13 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.043 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 01:08:47 | Hanwella (Kelani Ganga) | 4.24 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-10-06 02:29:03 | Magura (Kalu Ganga) | 3.22 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-06 02:05:22 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-06 02:05:55 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-06 02:01:51 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-06 02:06:13 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-06 02:10:58 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-06 02:16:56 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-06 02:00:13 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-06 02:20:24 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-06 02:03:36 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-06 02:02:38 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 02:20:02 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-06 02:00:15 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 02:02:28 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:01:43 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:02:55 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:02:25 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:04:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:01:34 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:02:30 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:05:06 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:24:03 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:03:21 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-06 01:29:27 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.010 |  |
| 2026-10-06 01:05:47 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-06 02:02:38 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-06 02:12:43 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-10-06 02:06:38 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-10-06 01:03:14 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.022 |  |
| 2026-10-06 02:12:24 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.026 |  |
| 2026-10-06 02:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.032 |  |
| 2026-10-06 02:13:23 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.043 |  |
| 2026-10-05 22:04:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.048 |  |
| 2026-10-06 02:00:32 | Glencourse (Kelani Ganga) | 13.00 | 🟢 Normal | -0.062 |  |
| 2026-10-06 02:08:09 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.098 |  |
| 2026-10-06 02:02:19 | Peradeniya (Mahaweli Ganga) | 3.49 | 🟢 Normal | -0.117 |  |
| 2026-10-06 02:03:42 | Thawalama (Gin Ganga) | 2.91 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)