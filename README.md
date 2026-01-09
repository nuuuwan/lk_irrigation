# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_10:01:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,760 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 10:01:29 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.130 |  |
| 2026-01-09 10:01:10 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:01:07 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:01:07 | Moragaswewa (Deduru Oya) | 2.50 | 🟢 Normal | -0.100 |  |
| 2026-01-09 10:00:43 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:00:12 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 10:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:00:09 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-09 09:17:09 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-09 09:13:14 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-09 09:11:31 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 09:09:54 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.009 |  |
| 2026-01-09 09:08:58 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-09 09:08:09 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-01-09 09:07:23 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-09 09:07:09 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.022 |  |
| 2026-01-09 09:06:00 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-09 09:05:30 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-01-09 09:05:26 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.028 |  |
| 2026-01-09 09:05:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.130 |  |
| 2026-01-09 09:05:09 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 09:05:02 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.071 |  |
| 2026-01-09 09:04:55 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 09:04:29 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-01-09 09:04:05 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 09:04:00 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 09:02:11 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-01-09 09:13:14 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-09 09:01:16 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-09 09:04:55 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 09:07:23 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-09 09:05:09 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 09:03:11 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 10:00:12 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 09:03:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 09:02:25 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:01:10 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 09:03:15 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 09:03:05 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:00:43 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 09:04:00 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 09:17:09 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-09 09:03:01 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:01:07 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-09 09:02:28 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 09:04:05 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 09:09:54 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.009 |  |
| 2026-01-09 09:05:30 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-01-09 09:06:00 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-09 09:04:29 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-01-09 09:08:58 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:00:09 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-09 09:08:09 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-01-09 09:01:42 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-01-09 09:03:06 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-01-09 09:01:45 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-01-09 09:01:13 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.022 |  |
| 2026-01-09 09:07:09 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.022 |  |
| 2026-01-09 09:05:26 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.028 |  |
| 2026-01-09 09:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.060 |  |
| 2026-01-09 09:05:02 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.071 |  |
| 2026-01-09 09:01:36 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.095 |  |
| 2026-01-09 10:01:07 | Moragaswewa (Deduru Oya) | 2.50 | 🟢 Normal | -0.100 |  |
| 2026-01-09 10:01:29 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)