# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--10_13:01:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **94,336 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 13:01:20 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:01:00 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-10 13:00:52 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-03-10 13:00:41 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-10 12:57:45 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-03-10 12:14:32 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.035 |  |
| 2026-03-10 12:10:23 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:09:39 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:08:44 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:08:27 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:07:04 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 13:00:41 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-10 12:02:54 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-10 13:01:00 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-10 12:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 12:02:15 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:01:35 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:01:20 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:04:56 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:03:07 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:01:40 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:04:23 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:08:27 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:01:39 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:02:28 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:10:23 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:02:59 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:03:03 | Moraketiya (Walawe Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:08:44 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:01:16 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:02:35 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:02:48 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:01:23 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:03:30 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:09:39 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:07:04 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:03:21 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-03-10 13:00:52 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-03-10 12:01:41 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.010 |  |
| 2026-03-10 12:04:11 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-03-10 12:03:20 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.012 |  |
| 2026-03-10 12:05:12 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.019 |  |
| 2026-03-10 12:00:58 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-03-10 12:57:45 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-03-10 12:03:16 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.030 |  |
| 2026-03-10 12:14:32 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.035 |  |
| 2026-03-10 12:02:38 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.039 |  |
| 2026-03-10 12:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.040 |  |
| 2026-03-10 12:04:01 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.083 |  |
| 2026-03-10 12:01:55 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)