# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_06:02:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,281 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 06:02:33 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.031 |  |
| 2026-06-10 06:02:21 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.026 |  |
| 2026-06-10 06:02:18 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.060 |  |
| 2026-06-10 06:02:16 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | -0.020 |  |
| 2026-06-10 06:02:12 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:01:59 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.037 |  |
| 2026-06-10 06:01:39 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:01:30 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:01:29 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:01:14 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-06-10 06:01:12 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:00:35 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-10 05:42:28 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-10 05:35:09 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 05:24:20 | Ellagawa (Kalu Ganga) | 5.84 | 🟢 Normal | -0.007 |  |
| 2026-06-10 05:15:25 | Rathnapura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.026 |  |
| 2026-06-10 05:13:17 | Dunamale (Aththanagalu Oya) | 1.91 | 🟢 Normal | -0.037 |  |
| 2026-06-10 05:13:15 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.285 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 05:13:15 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-06-10 06:01:14 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-06-10 05:10:52 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-10 04:01:02 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 05:04:56 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 06:00:35 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-10 06:02:12 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:01:12 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:01:39 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 05:04:21 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:03:19 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:01:30 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 02:05:44 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 05:03:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-10 05:01:19 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-10 05:02:40 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-10 05:03:02 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:12:11 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:01:29 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-10 05:02:51 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 05:24:20 | Ellagawa (Kalu Ganga) | 5.84 | 🟢 Normal | -0.007 |  |
| 2026-06-10 05:05:39 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-06-10 05:10:04 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-06-10 05:04:12 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-06-10 05:02:18 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-06-10 04:02:34 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-10 05:03:34 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-06-10 05:04:28 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-06-10 05:02:46 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-06-10 05:04:33 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-06-10 06:02:16 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | -0.020 |  |
| 2026-06-10 05:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-06-10 03:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.023 |  |
| 2026-06-10 06:02:21 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.026 |  |
| 2026-06-10 06:02:33 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.031 |  |
| 2026-06-10 06:01:59 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.037 |  |
| 2026-06-10 05:03:38 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.055 |  |
| 2026-06-10 05:10:38 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.058 |  |
| 2026-06-10 06:02:18 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)