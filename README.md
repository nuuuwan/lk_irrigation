# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_01:16:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,424 measurements** from **39** stations.
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
| 2026-10-12 01:16:28 | Magura (Kalu Ganga) | 3.43 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-10-12 01:14:35 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.028 |  |
| 2026-10-12 01:13:44 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.028 |  |
| 2026-10-12 01:09:16 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:07:53 | Giriulla (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:07:49 | Giriulla (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:07:47 | Urawa (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.029 |  |
| 2026-10-12 01:07:27 | Rathnapura (Kalu Ganga) | 3.39 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-10-12 01:07:22 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-10-12 01:06:57 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.118 |  |
| 2026-10-12 01:06:22 | Dunamale (Aththanagalu Oya) | 2.73 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-12 01:06:15 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.052 |  |
| 2026-10-12 01:05:49 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:05:31 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-12 01:05:09 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-12 01:04:39 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-12 01:04:14 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.103 |  |
| 2026-10-12 01:04:12 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.004 |  |
| 2026-10-12 01:03:31 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-10-12 01:03:08 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-12 01:02:26 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-12 01:02:20 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.021 |  |
| 2026-10-12 01:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.36 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-12 01:02:08 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:02:00 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | -0.060 |  |
| 2026-10-12 01:01:58 | Thawalama (Gin Ganga) | 3.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 01:01:25 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:01:22 | Ellagawa (Kalu Ganga) | 7.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 01:01:04 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:01:00 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:00:35 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 01:07:27 | Rathnapura (Kalu Ganga) | 3.39 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-10-12 01:16:28 | Magura (Kalu Ganga) | 3.43 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-10-12 01:07:22 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-10-12 01:05:31 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-12 01:05:09 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-12 01:06:22 | Dunamale (Aththanagalu Oya) | 2.73 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-11 23:00:24 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-12 01:04:39 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-12 00:02:26 | Panadugama (Nilwala Ganga) | 4.85 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-12 01:03:08 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-12 01:02:26 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-12 01:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.36 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-12 01:01:58 | Thawalama (Gin Ganga) | 3.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 01:01:22 | Ellagawa (Kalu Ganga) | 7.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 18:00:16 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 01:04:12 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.004 |  |
| 2026-10-12 00:03:24 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:07:53 | Giriulla (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:01:04 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:06:55 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:09:16 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:00:35 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:01:00 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:05:49 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-12 00:05:34 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:01:25 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-12 01:02:08 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-12 00:06:43 | Pitabeddara (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-10-11 18:02:15 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-10-12 01:03:31 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-10-12 00:03:27 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-10-12 01:02:20 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.021 |  |
| 2026-10-12 01:14:35 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.028 |  |
| 2026-10-12 01:13:44 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.028 |  |
| 2026-10-12 01:07:47 | Urawa (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.029 |  |
| 2026-10-12 01:06:15 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.052 |  |
| 2026-10-12 01:02:00 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | -0.060 |  |
| 2026-10-12 01:04:14 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.103 |  |
| 2026-10-12 01:06:57 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)