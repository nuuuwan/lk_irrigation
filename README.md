# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_18:19:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,001 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 18:19:40 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:14:32 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:14:31 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-24 18:12:16 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:10:23 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:08:23 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:08:06 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.046 |  |
| 2026-02-24 18:07:05 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:06:20 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-24 18:06:14 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:06:10 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.045 |  |
| 2026-02-24 18:05:51 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:04:59 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-24 18:04:47 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-02-24 18:03:45 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:03:23 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-02-24 18:03:16 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:03:13 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:02:58 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:02:39 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:02:38 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:02:37 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.053 |  |
| 2026-02-24 18:02:17 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.051 |  |
| 2026-02-24 18:02:16 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-02-24 18:02:08 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:02:06 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -0.022 |  |
| 2026-02-24 18:02:05 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:01:57 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-24 18:01:47 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-02-24 18:01:39 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | -0.039 |  |
| 2026-02-24 18:01:38 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:01:35 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:01:33 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:01:23 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.011 |  |
| 2026-02-24 18:01:21 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-24 18:01:19 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:01:10 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-24 18:01:07 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:00:13 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-02-24 17:46:07 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | -0.039 |  |
| 2026-02-24 17:31:03 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 18:02:16 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-02-24 18:06:20 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-24 18:01:10 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-24 18:04:59 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-24 18:14:31 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-24 18:01:35 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:02:05 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:03:13 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:01:19 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:02:38 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:03:16 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:01:33 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:02:39 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:02:37 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:06:14 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-24 17:01:48 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:07:05 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:10:23 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:02:58 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:02:08 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:05:51 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:12:16 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:03:45 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:19:40 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:14:32 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:01:38 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:01:21 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-24 18:01:57 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-24 18:01:23 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.011 |  |
| 2026-02-24 18:04:47 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-02-24 18:03:23 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-02-24 18:00:13 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-02-24 18:02:06 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -0.022 |  |
| 2026-02-24 18:01:47 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-02-24 18:01:39 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | -0.039 |  |
| 2026-02-24 18:06:10 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.045 |  |
| 2026-02-24 18:08:06 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.046 |  |
| 2026-02-24 18:02:17 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.051 |  |
| 2026-02-24 18:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)