# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_16:01:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **230,656 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **5** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 16:01:00 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:00:53 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:00:48 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:58:00 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.536 | 🔺 Rising |
| 2026-08-11 15:22:13 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 15:58:00 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.536 | 🔺 Rising |
| 2026-08-11 15:03:49 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-08-11 15:01:32 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-11 15:03:27 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-11 15:02:24 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 15:00:43 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:00:48 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:01:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:04:15 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:00:03 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:03:09 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:02:57 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:04:10 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:08:32 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:04:08 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:03:59 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:05:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:03:17 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:22:13 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:03:07 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:08:14 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:01:49 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:01:00 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:00:53 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-08-11 15:06:55 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-08-11 15:03:29 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-08-11 15:02:58 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-08-11 15:04:08 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.012 |  |
| 2026-08-11 15:07:27 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-08-11 15:03:56 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.020 |  |
| 2026-08-11 15:03:30 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.020 |  |
| 2026-08-11 15:01:14 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.030 |  |
| 2026-08-11 15:10:25 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.047 |  |
| 2026-08-11 15:08:08 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.062 |  |
| 2026-08-11 15:04:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.062 |  |
| 2026-08-11 15:11:16 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.064 |  |
| 2026-08-11 15:01:32 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)