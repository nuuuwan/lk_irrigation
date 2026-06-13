# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_07:00:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,001 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 07:00:47 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-13 06:42:08 | Galgamuwa (Mee Oya) | 1.58 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-13 06:11:15 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 06:00:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.34 | 🟡 Alert | 0.054 | 🔺 Rising |
| 2026-06-13 06:03:46 | Magura (Kalu Ganga) | 4.52 | 🟡 Alert | -0.091 |  |
| 2026-06-13 06:00:45 | Rathnapura (Kalu Ganga) | 6.00 | 🟡 Alert | -0.105 |  |
| 2026-06-13 06:05:24 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-06-13 06:42:08 | Galgamuwa (Mee Oya) | 1.58 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-13 06:03:07 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-13 06:04:51 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-13 06:07:43 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-13 06:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-13 06:02:24 | Dunamale (Aththanagalu Oya) | 3.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 06:04:48 | Baddegama (Gin Ganga) | 3.15 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-13 06:00:41 | Putupaula (Kalu Ganga) | 2.39 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-13 06:00:47 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-13 06:00:49 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 06:00:16 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 05:03:38 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 06:02:21 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 06:03:53 | Ellagawa (Kalu Ganga) | 8.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 06:02:04 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-06-13 07:00:47 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-13 06:03:50 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-13 06:03:56 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-13 06:02:49 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-13 06:02:39 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-13 06:03:00 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:19:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-13 06:01:27 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-13 06:04:23 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 06:01:57 | Badalgama (Maha Oya) | 3.37 | 🟢 Normal | -0.010 |  |
| 2026-06-13 06:05:06 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.021 |  |
| 2026-06-13 06:11:15 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-06-13 06:05:39 | Panadugama (Nilwala Ganga) | 4.84 | 🟢 Normal | -0.029 |  |
| 2026-06-13 06:07:50 | Hanwella (Kelani Ganga) | 4.16 | 🟢 Normal | -0.037 |  |
| 2026-06-13 06:01:17 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.053 |  |
| 2026-06-13 06:06:12 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | -0.066 |  |
| 2026-06-13 06:03:39 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.073 |  |
| 2026-06-13 06:04:10 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.114 |  |
| 2026-06-13 06:00:17 | Pitabeddara (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.128 |  |
| 2026-06-13 06:05:33 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)