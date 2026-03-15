# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_19:17:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,273 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 19:17:57 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:14:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.025 |  |
| 2026-03-15 19:12:24 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-15 19:11:17 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.085 |  |
| 2026-03-15 19:10:25 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-03-15 19:09:41 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:09:06 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.045 |  |
| 2026-03-15 19:07:35 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:07:32 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:07:30 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 19:07:12 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.027 |  |
| 2026-03-15 19:07:12 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.009 |  |
| 2026-03-15 19:06:58 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-15 19:06:08 | Kithulgala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.074 |  |
| 2026-03-15 19:05:05 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-15 19:05:00 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-03-15 19:04:20 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-15 19:04:19 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:04:13 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:03:49 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-03-15 19:03:40 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-15 19:03:38 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:03:24 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:03:08 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:03:06 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:02:23 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-03-15 19:02:21 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:02:19 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:02:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:01:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.033 |  |
| 2026-03-15 19:01:54 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 19:01:53 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:01:30 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:01:13 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:00:55 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.037 |  |
| 2026-03-15 19:00:47 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-15 19:00:41 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:00:11 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 19:03:40 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-15 19:04:20 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-15 19:12:24 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-15 19:00:11 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-15 19:01:54 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 19:07:30 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 19:09:41 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:03:08 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:00:41 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:01:53 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:04:19 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:03:24 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:05:04 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:04:13 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:03:38 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:02:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:07:32 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:07:35 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:02:20 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:02:21 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:17:57 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:01:13 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:01:30 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:10:25 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-03-15 19:07:12 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.009 |  |
| 2026-03-15 19:06:58 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-15 19:00:47 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-15 19:05:05 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-15 19:05:00 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-03-15 19:03:49 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-03-15 19:02:23 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-03-15 19:14:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.025 |  |
| 2026-03-15 19:07:12 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.027 |  |
| 2026-03-15 19:01:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.033 |  |
| 2026-03-15 19:00:55 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.037 |  |
| 2026-03-15 18:02:59 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.040 |  |
| 2026-03-15 19:09:06 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.045 |  |
| 2026-03-15 19:06:08 | Kithulgala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.074 |  |
| 2026-03-15 19:11:17 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)