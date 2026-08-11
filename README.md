# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_15:01:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **230,618 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 15:01:14 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.030 |  |
| 2026-08-11 15:01:07 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:01:05 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:00:43 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:00:26 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:00:03 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:48:39 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.006 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 14:04:50 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-11 14:01:58 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 14:06:00 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 15:00:43 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:00:26 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:01:34 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:00:03 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:02:14 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:04:49 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:03:09 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:09:54 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:10:23 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:00:06 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:07:10 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:07:59 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:01:07 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:01:26 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:07:32 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:01:05 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:01:52 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-08-11 14:48:39 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.006 |  |
| 2026-08-11 14:12:29 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-08-11 14:07:29 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-08-11 14:03:57 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-08-11 14:01:39 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-08-11 14:05:35 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.016 |  |
| 2026-08-11 14:03:52 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.022 |  |
| 2026-08-11 14:05:33 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-08-11 15:01:14 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.030 |  |
| 2026-08-11 14:02:12 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-08-11 14:08:45 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.040 |  |
| 2026-08-11 14:01:28 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.040 |  |
| 2026-08-11 14:03:00 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.046 |  |
| 2026-08-11 14:03:03 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.053 |  |
| 2026-08-11 14:04:36 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.070 |  |
| 2026-08-11 14:06:38 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)