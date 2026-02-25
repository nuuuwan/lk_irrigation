# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_10:21:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,582 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 10:21:58 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.008 |  |
| 2026-02-25 10:18:50 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-25 10:11:22 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.009 |  |
| 2026-02-25 10:08:45 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-25 10:08:26 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.030 |  |
| 2026-02-25 10:07:55 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:07:22 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-02-25 10:06:34 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.068 |  |
| 2026-02-25 10:06:03 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:05:43 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-02-25 10:04:53 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:04:43 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:04:24 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:04:12 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:03:56 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:03:55 | Dunamale (Aththanagalu Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:03:53 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:03:51 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:03:43 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:03:23 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:03:19 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-25 10:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.030 |  |
| 2026-02-25 10:02:50 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:02:48 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:02:36 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-25 10:02:24 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:02:20 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:02:19 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:01:51 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.051 |  |
| 2026-02-25 10:01:48 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:01:46 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 10:01:43 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:01:41 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 10:01:33 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-02-25 10:01:15 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 10:01:11 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.062 |  |
| 2026-02-25 10:00:33 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 10:01:33 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-02-25 10:18:50 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-25 10:03:19 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-25 10:01:46 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 10:01:15 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 10:01:41 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 10:08:45 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-25 10:02:36 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-25 10:03:43 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:01:43 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:02:19 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:04:24 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:00:33 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:04:53 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:02:20 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:02:48 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:04:12 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:03:53 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-25 09:06:05 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:01:48 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:02:24 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:21:58 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.008 |  |
| 2026-02-25 10:07:22 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-02-25 10:11:22 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.009 |  |
| 2026-02-25 10:04:43 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:03:23 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:02:50 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:06:03 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:07:55 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:03:55 | Dunamale (Aththanagalu Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:03:56 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:03:51 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-25 10:05:43 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-02-25 10:08:26 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.030 |  |
| 2026-02-25 10:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.030 |  |
| 2026-02-25 10:01:51 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.051 |  |
| 2026-02-25 10:01:11 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.062 |  |
| 2026-02-25 10:06:34 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)