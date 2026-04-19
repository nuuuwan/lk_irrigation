# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_14:34:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,345 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 14:34:23 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:16:04 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-04-19 14:12:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.018 |  |
| 2026-04-19 14:09:15 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-19 14:08:49 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:07:37 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-04-19 14:07:20 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 14:02:41 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-04-19 14:02:45 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 14:09:15 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-19 13:32:57 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-19 14:02:16 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:02:00 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:01:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:02:13 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:05:39 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:04:18 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:02:15 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:02:48 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:04:12 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:04:51 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:01:46 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:04:24 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:05:09 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:34:23 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:08:49 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:00:52 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:02:14 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:02:00 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-19 14:16:04 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-04-19 14:06:41 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-04-19 14:07:37 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-04-19 14:03:32 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-19 14:01:32 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-19 14:02:07 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | -0.011 |  |
| 2026-04-19 14:12:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.018 |  |
| 2026-04-19 14:04:45 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-04-19 14:03:55 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.019 |  |
| 2026-04-19 14:01:51 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | -0.023 |  |
| 2026-04-19 14:07:20 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.029 |  |
| 2026-04-19 14:01:12 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.030 |  |
| 2026-04-19 14:05:08 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.037 |  |
| 2026-04-19 06:01:33 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.086 |  |
| 2026-04-19 14:05:35 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.105 |  |
| 2026-04-19 14:00:46 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.209 |  |
| 2026-04-19 14:04:30 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -1.565 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)