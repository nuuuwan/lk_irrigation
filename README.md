# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_05:34:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,247 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 05:34:07 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.056 |  |
| 2026-02-01 05:27:21 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:12:41 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 05:11:47 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.036 |  |
| 2026-02-01 05:10:27 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:09:30 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 05:08:33 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:07:02 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-01 05:06:43 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-01 05:06:01 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:05:45 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-01 05:04:51 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.005 |  |
| 2026-02-01 05:04:38 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.050 |  |
| 2026-02-01 05:04:35 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.013 |  |
| 2026-02-01 05:03:56 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:56 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-01 05:03:43 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:42 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:42 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:41 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:40 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:40 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:39 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:37 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:36 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:24 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:08 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -2.700 |  |
| 2026-02-01 05:03:07 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.082 |  |
| 2026-02-01 05:03:07 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:02:51 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:02:40 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:02:28 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-02-01 05:02:28 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -2.700 |  |
| 2026-02-01 05:02:18 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 05:02:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.152 |  |
| 2026-02-01 05:02:03 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.056 |  |
| 2026-02-01 05:01:53 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:01:09 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-02-01 05:00:55 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:00:45 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.074 |  |
| 2026-02-01 05:00:30 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:42:44 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 03:04:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 1.688 | 🔺 Rising |
| 2026-02-01 05:07:02 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-01 05:03:56 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-01 05:05:45 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-01 05:02:18 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 05:12:41 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 05:09:30 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 05:04:51 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.005 |  |
| 2026-02-01 05:00:30 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:01:53 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:23:25 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:02:51 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:10:27 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:08:19 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:06:01 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:01:12 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:24 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:42 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:08:33 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:00:55 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:07 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:43 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:02:40 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:03:56 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:27:21 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:52 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:06:43 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-01 05:02:28 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-02-01 05:04:35 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.013 |  |
| 2026-02-01 05:01:09 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-02-01 05:11:47 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.036 |  |
| 2026-02-01 05:04:38 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.050 |  |
| 2026-01-31 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.051 |  |
| 2026-02-01 05:34:07 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.056 |  |
| 2026-02-01 05:00:45 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.074 |  |
| 2026-02-01 05:03:07 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.082 |  |
| 2026-02-01 05:02:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.152 |  |
| 2026-02-01 05:03:08 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -2.700 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)