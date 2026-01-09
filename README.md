# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_21:11:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,220 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 21:11:59 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-01-09 21:09:53 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:09:32 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:07:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-09 21:07:20 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:07:08 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:06:31 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:06:26 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.076 |  |
| 2026-01-09 21:05:52 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:05:32 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.020 |  |
| 2026-01-09 21:05:20 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-01-09 21:04:49 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:04:44 | Manampitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.057 |  |
| 2026-01-09 21:04:26 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:04:04 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:03:47 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:03:45 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:03:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.061 |  |
| 2026-01-09 21:03:17 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.089 |  |
| 2026-01-09 21:03:02 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:02:55 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:02:44 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:02:35 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:02:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-09 21:02:14 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:02:11 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 21:02:11 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.010 |  |
| 2026-01-09 21:01:58 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-09 21:01:51 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:01:48 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-01-09 21:01:43 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:01:26 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:01:11 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:00:56 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-09 21:00:11 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.120 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 21:11:59 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-01-09 21:00:11 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-09 17:13:03 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 21:02:11 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 21:07:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-09 21:03:45 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:01:26 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:04:04 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:02:44 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:02:14 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:06:31 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:03:02 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:07:08 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:09:53 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:05:52 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:07:20 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:03:47 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:09:32 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:02:55 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:01:51 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:04:26 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:01:43 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:38:21 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:01:11 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:04:49 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-09 21:05:20 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-01-09 21:02:11 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.010 |  |
| 2026-01-09 21:02:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-09 21:01:58 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-09 21:00:56 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:08:00 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-09 21:01:48 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-01-09 21:05:32 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.020 |  |
| 2026-01-09 21:04:44 | Manampitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.057 |  |
| 2026-01-09 21:03:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.061 |  |
| 2026-01-09 21:06:26 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.076 |  |
| 2026-01-09 21:03:17 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)