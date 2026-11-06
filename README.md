# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_13:03:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,427 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 13:03:27 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.030 |  |
| 2026-11-06 13:03:16 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 13:03:07 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-06 13:03:05 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:02:58 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:02:53 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:02:37 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.11 | 🟢 Normal | -0.062 |  |
| 2026-11-06 13:02:16 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-06 13:02:09 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.021 |  |
| 2026-11-06 13:02:04 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.041 |  |
| 2026-11-06 13:01:59 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:56 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:39 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:38 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:34 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:33 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 13:01:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:17 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-11-06 13:01:13 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:00:12 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.181 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 13:03:07 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-06 13:02:16 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-06 12:00:55 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-06 13:03:16 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 13:01:33 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 13:01:59 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:38 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:02:53 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:02:37 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-11-06 12:05:09 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:39 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:13 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-06 12:02:53 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:02:58 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:56 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:03:05 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-06 12:18:02 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:34 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-06 12:19:55 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-06 12:04:19 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-11-06 12:04:11 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.011 |  |
| 2026-11-06 12:05:46 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.019 |  |
| 2026-11-06 12:05:28 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.019 |  |
| 2026-11-06 12:05:25 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.020 |  |
| 2026-11-06 13:01:17 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-11-06 13:02:09 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.021 |  |
| 2026-11-06 12:05:04 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.029 |  |
| 2026-11-06 13:03:27 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.030 |  |
| 2026-11-06 12:04:24 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.036 |  |
| 2026-11-06 13:02:04 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.041 |  |
| 2026-11-06 12:02:43 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.042 |  |
| 2026-11-06 12:01:32 | Moragaswewa (Deduru Oya) | 2.83 | 🟢 Normal | -0.050 |  |
| 2026-11-06 12:04:38 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.059 |  |
| 2026-11-06 12:03:53 | Panadugama (Nilwala Ganga) | 3.91 | 🟢 Normal | -0.061 |  |
| 2026-11-06 13:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.11 | 🟢 Normal | -0.062 |  |
| 2026-11-06 13:00:12 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.181 |  |
| 2026-11-06 12:08:45 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.190 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)