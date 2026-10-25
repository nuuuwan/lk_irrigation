# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_08:13:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,385 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 08:13:25 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-25 08:13:15 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:12:06 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-25 08:11:58 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -0.008 |  |
| 2026-10-25 08:10:29 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:10:19 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-25 08:07:40 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:07:28 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:06:15 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:06:13 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-25 08:06:12 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 08:05:43 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:04:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-25 08:04:28 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | -0.029 |  |
| 2026-10-25 08:04:05 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -0.095 |  |
| 2026-10-25 08:04:04 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:04:03 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-25 08:03:59 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.087 |  |
| 2026-10-25 08:03:46 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-10-25 08:03:45 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-10-25 08:03:44 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:03:36 | Ellagawa (Kalu Ganga) | 6.22 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-25 08:03:33 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | -0.010 |  |
| 2026-10-25 08:03:17 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 08:03:13 | Rathnapura (Kalu Ganga) | 3.52 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-10-25 08:03:11 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 08:03:00 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:03:00 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:02:16 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-25 08:02:12 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:01:57 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 08:01:54 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-25 08:01:44 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.059 |  |
| 2026-10-25 08:01:39 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.147 |  |
| 2026-10-25 08:01:38 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-10-25 08:01:33 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 08:01:05 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-10-25 08:00:57 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 08:00:37 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 08:03:46 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-10-25 08:03:13 | Rathnapura (Kalu Ganga) | 3.52 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-10-25 08:10:19 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-25 08:06:13 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-25 08:04:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-25 08:03:36 | Ellagawa (Kalu Ganga) | 6.22 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-25 08:01:54 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-25 08:02:16 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-25 08:12:06 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-25 08:03:17 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 08:00:57 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 08:01:33 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 08:03:11 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 08:06:12 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 08:13:25 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-25 08:01:57 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 08:03:00 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:00:37 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:05:43 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:07:40 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:10:29 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:03:44 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:07:28 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:03:00 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:06:15 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:13:15 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:04:04 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:02:12 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-25 08:11:58 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -0.008 |  |
| 2026-10-25 08:04:03 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-25 08:01:05 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-10-25 08:03:33 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | -0.010 |  |
| 2026-10-25 08:01:38 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-10-25 08:03:45 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-10-25 08:04:28 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | -0.029 |  |
| 2026-10-25 08:01:44 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.059 |  |
| 2026-10-25 08:03:59 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.087 |  |
| 2026-10-25 08:04:05 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -0.095 |  |
| 2026-10-25 08:01:39 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)