# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_15:12:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,664 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 15:12:59 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:10:21 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 15:07:46 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.023 |  |
| 2026-06-10 15:07:01 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.022 |  |
| 2026-06-10 15:06:44 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:05:58 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:05:44 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:05:31 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-06-10 15:05:04 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:04:43 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-06-10 15:04:30 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:04:20 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:04:15 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-10 15:04:08 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:03:52 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:03:52 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:03:47 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:03:47 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | -0.012 |  |
| 2026-06-10 15:03:42 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | -0.010 |  |
| 2026-06-10 15:03:36 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.059 |  |
| 2026-06-10 15:03:32 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:03:31 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | -0.039 |  |
| 2026-06-10 15:03:27 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:03:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:03:19 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-06-10 15:03:06 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | -0.020 |  |
| 2026-06-10 15:03:00 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-06-10 15:03:00 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-06-10 15:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | -0.010 |  |
| 2026-06-10 15:02:06 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:01:47 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.050 |  |
| 2026-06-10 15:01:36 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:01:26 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:01:10 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-06-10 15:01:07 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.044 |  |
| 2026-06-10 15:01:06 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:00:52 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:00:29 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 15:10:21 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 15:06:44 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:01:26 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:05:44 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:05:04 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:03:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:00:29 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:05:58 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:00:52 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:03:32 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:03:27 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:12:59 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:04:30 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:04:20 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:01:06 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:03:47 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:03:52 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:02:06 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:03:52 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:01:36 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-10 15:03:42 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | -0.010 |  |
| 2026-06-10 15:05:31 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-06-10 15:04:43 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-06-10 15:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | -0.010 |  |
| 2026-06-10 15:03:00 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-06-10 15:03:19 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-06-10 15:04:15 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-10 15:03:47 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | -0.012 |  |
| 2026-06-10 14:02:57 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.012 |  |
| 2026-06-10 15:03:06 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | -0.020 |  |
| 2026-06-10 15:03:00 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-06-10 15:07:01 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.022 |  |
| 2026-06-10 15:07:46 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.023 |  |
| 2026-06-10 15:01:10 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-06-10 15:03:31 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | -0.039 |  |
| 2026-06-10 15:01:07 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.044 |  |
| 2026-06-10 15:01:47 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.050 |  |
| 2026-06-10 15:03:36 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)