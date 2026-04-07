# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_21:00:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,902 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 21:00:16 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:35:06 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.059 |  |
| 2026-04-07 20:17:44 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-07 20:11:59 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:09:19 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-07 20:08:45 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:07:24 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 20:01:39 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-07 20:17:44 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-07 20:09:19 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-07 20:02:39 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 20:03:52 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 21:00:16 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:04:22 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:11:59 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:02:55 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:03:29 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:07:24 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:03:18 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:06:04 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:05:56 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:04:33 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:01:30 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:02:50 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:05:50 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:05:11 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:08:45 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:05:27 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:05:33 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:01:09 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:00:51 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-07 20:04:27 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-04-07 20:02:48 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-07 20:03:43 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-07 20:04:51 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.010 |  |
| 2026-04-07 18:00:44 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-04-07 20:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.012 |  |
| 2026-04-07 20:02:10 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-04-07 20:06:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.022 |  |
| 2026-04-07 20:03:26 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.023 |  |
| 2026-04-07 20:06:53 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.029 |  |
| 2026-04-07 18:02:51 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.032 |  |
| 2026-04-07 20:35:06 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.059 |  |
| 2026-04-07 18:01:46 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.060 |  |
| 2026-04-07 20:03:29 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.060 |  |
| 2026-04-07 20:02:11 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)