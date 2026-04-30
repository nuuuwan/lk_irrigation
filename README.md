# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_06:37:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,847 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 06:37:52 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.007 |  |
| 2026-04-30 06:36:36 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-30 06:17:35 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:08:58 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.028 |  |
| 2026-04-30 06:08:12 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-30 06:07:59 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.027 |  |
| 2026-04-30 06:07:25 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.560 | 🔺 Rising |
| 2026-04-30 06:06:36 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:06:29 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.023 |  |
| 2026-04-30 06:06:05 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.059 |  |
| 2026-04-30 06:05:58 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.009 |  |
| 2026-04-30 06:05:55 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 06:05:32 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-30 06:05:31 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-30 06:05:25 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:05:07 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-30 06:05:07 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:04:57 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.028 |  |
| 2026-04-30 06:03:53 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.022 |  |
| 2026-04-30 06:03:45 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.005 |  |
| 2026-04-30 06:03:24 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-30 06:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | -0.051 |  |
| 2026-04-30 06:03:15 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-04-30 06:03:01 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-04-30 06:02:58 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:02:33 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:02:30 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-30 06:02:26 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-30 06:02:07 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.002 |  |
| 2026-04-30 06:01:59 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:01:52 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 06:01:51 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-04-30 06:01:32 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.079 |  |
| 2026-04-30 06:01:24 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.037 |  |
| 2026-04-30 06:01:10 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-30 06:01:03 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-04-30 06:00:56 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-04-30 06:00:28 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-30 06:00:18 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 06:07:25 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.560 | 🔺 Rising |
| 2026-04-30 06:00:56 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-04-30 06:00:28 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-30 06:05:31 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-30 06:05:07 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-30 06:03:24 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-30 06:02:30 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-30 06:08:12 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-30 06:01:52 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 06:05:32 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-30 06:05:55 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 06:02:07 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.002 |  |
| 2026-04-30 06:01:59 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:06:36 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:00:18 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:05:25 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:02:58 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:17:35 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:02:33 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:03:45 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.005 |  |
| 2026-04-30 06:37:52 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.007 |  |
| 2026-04-30 06:05:58 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.009 |  |
| 2026-04-30 06:02:26 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-30 06:03:15 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-04-30 06:03:01 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-04-30 06:01:10 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-30 06:36:36 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-30 06:01:03 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-04-30 06:01:51 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-04-30 06:03:53 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.022 |  |
| 2026-04-30 06:06:29 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.023 |  |
| 2026-04-30 06:07:59 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.027 |  |
| 2026-04-30 06:08:58 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.028 |  |
| 2026-04-30 06:04:57 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.028 |  |
| 2026-04-30 06:01:24 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.037 |  |
| 2026-04-29 18:02:02 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-04-30 06:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | -0.051 |  |
| 2026-04-30 06:06:05 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.059 |  |
| 2026-04-30 06:01:32 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)