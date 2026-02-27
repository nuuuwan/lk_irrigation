# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--27_17:18:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **84,643 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 17:18:24 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:16:04 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-27 17:12:38 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 17:12:23 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:11:12 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-02-27 17:10:52 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-02-27 17:10:23 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:09:00 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:07:58 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-02-27 17:06:10 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:05:15 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:05:09 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.009 |  |
| 2026-02-27 17:04:52 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:04:40 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:04:38 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:04:33 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:04:23 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:03:40 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:03:13 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-02-27 17:03:10 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-02-27 17:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 17:02:27 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-27 17:02:25 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | -0.020 |  |
| 2026-02-27 17:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.030 |  |
| 2026-02-27 17:02:22 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:02:20 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-27 17:02:19 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:02:16 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-02-27 17:02:15 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 17:02:15 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:02:07 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:02:00 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:01:57 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:01:49 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.012 |  |
| 2026-02-27 17:01:36 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-27 17:01:26 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-02-27 17:01:06 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:01:05 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:00:50 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 17:02:20 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-27 17:02:27 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-27 17:01:36 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-27 17:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 17:12:38 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 17:02:15 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 17:16:04 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-27 17:02:22 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:02:00 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:00:32 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:12:23 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:05:15 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:01:05 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:10:23 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:09:00 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:02:15 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:04:40 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:00:50 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:04:23 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:18:24 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:04:33 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:01:06 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:04:38 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:06:10 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:03:40 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:04:52 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:01:57 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:02:19 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-27 17:10:52 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-02-27 17:11:12 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-02-27 17:05:09 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.009 |  |
| 2026-02-27 17:07:58 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-02-27 17:02:16 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-02-27 17:01:26 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-02-27 17:01:49 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.012 |  |
| 2026-02-27 17:02:25 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | -0.020 |  |
| 2026-02-27 17:03:10 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-02-27 17:03:13 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-02-27 17:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.030 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)