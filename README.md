# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_07:08:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,052 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 07:08:13 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:08:00 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.018 |  |
| 2026-04-10 07:07:07 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.064 |  |
| 2026-04-10 07:06:49 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.049 |  |
| 2026-04-10 07:06:44 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-04-10 07:05:53 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-10 07:05:39 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:05:16 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.414 | 🔺 Rising |
| 2026-04-10 07:04:54 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:04:36 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.022 |  |
| 2026-04-10 07:04:34 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 07:04:25 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:04:23 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-04-10 07:04:19 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.002 |  |
| 2026-04-10 07:04:19 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-04-10 07:03:32 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.022 |  |
| 2026-04-10 07:03:16 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:03:04 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-10 07:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-04-10 07:02:28 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:02:12 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-04-10 07:02:10 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.021 |  |
| 2026-04-10 07:02:09 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-04-10 07:02:09 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:02:08 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:02:06 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-10 07:01:56 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:01:55 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.065 |  |
| 2026-04-10 07:01:36 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.012 |  |
| 2026-04-10 07:01:10 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:01:09 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:01:03 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:00:43 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:00:36 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.014 |  |
| 2026-04-10 06:16:09 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 07:02:09 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-04-10 07:05:16 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.414 | 🔺 Rising |
| 2026-04-10 07:02:06 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-10 07:05:53 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-10 03:09:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-10 06:02:29 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-10 07:04:34 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 07:01:09 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:03:16 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:01:56 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:02:28 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:00:43 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:04:25 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:08:13 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:05:56 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:02:08 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:01:03 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:02:09 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:04:54 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-10 06:02:20 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:01:10 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:05:39 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-10 07:04:19 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.002 |  |
| 2026-04-10 07:06:44 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-04-10 07:04:23 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-04-10 07:03:04 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-10 07:01:36 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.012 |  |
| 2026-04-10 07:00:36 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.014 |  |
| 2026-04-10 07:08:00 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.018 |  |
| 2026-04-10 07:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-04-10 07:02:10 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.021 |  |
| 2026-04-10 07:04:19 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-04-10 07:03:32 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.022 |  |
| 2026-04-10 07:04:36 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.022 |  |
| 2026-04-10 07:02:12 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-04-10 07:06:49 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.049 |  |
| 2026-04-10 06:02:39 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.054 |  |
| 2026-04-10 07:07:07 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.064 |  |
| 2026-04-10 07:01:55 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)