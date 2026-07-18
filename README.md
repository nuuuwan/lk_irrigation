# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18_10:07:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **209,461 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-18 10:07:57 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-07-18 10:07:01 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:06:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:05:24 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:05:15 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:05:14 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:04:42 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:04:08 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-07-18 10:04:07 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:04:00 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-07-18 10:03:57 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.011 |  |
| 2026-07-18 10:03:16 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-07-18 10:02:59 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-07-18 10:02:56 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:55 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:52 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:47 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:32 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:19 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:10 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:04 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:53 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:47 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-18 10:01:45 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-07-18 10:01:42 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:40 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:40 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:22 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-18 10:01:20 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:18 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:11 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:09 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-18 10:01:09 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | -0.125 |  |
| 2026-07-18 10:00:47 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:00:23 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-18 10:04:08 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-07-18 10:03:16 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-07-18 10:01:09 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-18 10:01:47 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-18 09:06:33 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-18 10:01:22 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-18 10:01:40 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:20 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:42 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:52 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:53 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:07:01 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:32 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:55 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:05:15 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:11 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:04 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:00:23 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:40 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:19 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:04:07 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:05:14 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:47 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:01:18 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:00:47 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:04:42 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:05:24 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:56 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:02:10 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:06:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-18 10:04:00 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-07-18 10:07:57 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-07-18 10:02:59 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-07-18 09:06:32 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-07-18 10:03:57 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.011 |  |
| 2026-07-18 09:01:40 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.013 |  |
| 2026-07-18 10:01:45 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-07-18 10:01:09 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)