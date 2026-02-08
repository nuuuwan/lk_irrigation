# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_15:14:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,570 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 15:14:22 | Weraganthota (Mahaweli Ganga) | -2.22 | 🟢 Normal | -0.048 |  |
| 2026-02-08 15:12:35 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-08 15:12:15 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.017 |  |
| 2026-02-08 15:10:27 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:09:29 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:08:57 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:07:11 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-08 15:06:50 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:06:37 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.046 |  |
| 2026-02-08 15:06:08 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-02-08 15:05:26 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:05:19 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:04:53 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:04:38 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.010 |  |
| 2026-02-08 15:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | -0.050 |  |
| 2026-02-08 15:04:07 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.003 |  |
| 2026-02-08 15:03:50 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:03:44 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:03:39 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:03:27 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:03:24 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-02-08 15:03:14 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:03:04 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:02:59 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:02:57 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-02-08 15:02:56 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-02-08 15:02:48 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:02:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-08 15:02:46 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:02:38 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:02:32 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-02-08 15:02:11 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:02:05 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-02-08 15:01:56 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:01:45 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-08 15:01:29 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.021 |  |
| 2026-02-08 15:01:27 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:00:33 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-02-08 15:00:11 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 15:02:56 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-02-08 15:02:57 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-02-08 15:12:35 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-08 15:04:07 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.003 |  |
| 2026-02-08 15:01:27 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:03:39 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:02:59 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:03:27 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:03:44 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:05:26 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:10:27 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:04:53 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:02:38 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:03:14 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:02:48 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:09:29 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:03:04 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:03:50 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:06:50 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:02:11 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:02:46 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 14:02:47 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:01:56 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:05:19 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-08 15:02:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-08 15:02:05 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-02-08 15:01:45 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-08 15:03:24 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-02-08 15:00:33 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-02-08 15:04:38 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.010 |  |
| 2026-02-08 15:07:11 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-08 15:02:32 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-02-08 15:12:15 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.017 |  |
| 2026-02-08 15:06:08 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-02-08 15:01:29 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.021 |  |
| 2026-02-08 15:06:37 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.046 |  |
| 2026-02-08 15:14:22 | Weraganthota (Mahaweli Ganga) | -2.22 | 🟢 Normal | -0.048 |  |
| 2026-02-08 15:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)