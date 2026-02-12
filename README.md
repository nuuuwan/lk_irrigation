# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_17:14:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,223 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 17:14:04 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-02-12 17:10:08 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.018 |  |
| 2026-02-12 17:09:03 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 17:09:01 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:08:45 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:07:50 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:07:19 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:06:15 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-12 17:05:09 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:04:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:04:20 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-12 17:04:11 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-02-12 17:03:59 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-12 17:03:51 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:03:45 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:03:29 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:03:16 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:03:11 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 17:03:07 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:03:07 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-12 17:03:00 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:02:55 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:02:53 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:02:41 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:02:40 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-12 17:02:32 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-02-12 17:02:30 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:02:30 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 17:02:11 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 17:02:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:01:51 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:01:35 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:01:32 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:01:20 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-12 17:01:17 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 17:01:00 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-12 17:00:57 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-12 17:00:56 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-12 17:00:32 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 17:04:11 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-02-12 17:01:20 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-12 17:00:56 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-12 17:03:07 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-12 17:02:40 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-12 17:02:11 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 17:01:17 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 17:03:11 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 17:09:03 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 17:02:30 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 17:01:32 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:08:45 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:02:53 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:02:30 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:03:07 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:01:51 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:02:55 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:03:16 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:07:19 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:00:32 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:01:35 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:03:00 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:02:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:05:09 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:03:29 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:03:45 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:09:01 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:02:41 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:07:50 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:04:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-12 17:14:04 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-02-12 17:04:20 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-12 17:03:59 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-12 17:06:15 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-12 17:01:00 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-12 17:00:57 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-12 17:02:32 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-02-12 17:10:08 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.018 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)