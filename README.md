# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--27_10:16:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **84,365 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 10:16:49 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.008 |  |
| 2026-02-27 10:16:16 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:09:33 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-27 10:08:58 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:08:32 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-27 10:08:29 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:07:59 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:07:29 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-27 10:07:27 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.019 |  |
| 2026-02-27 10:07:04 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:06:56 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:06:05 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:05:41 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:04:46 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-27 10:04:24 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:03:52 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-27 10:03:49 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:03:46 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:03:30 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:03:27 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-27 10:03:26 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-27 10:03:24 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.049 |  |
| 2026-02-27 10:02:39 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-02-27 10:02:26 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-27 10:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:02:12 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:02:12 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:02:09 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-02-27 10:02:04 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-27 10:02:02 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:01:55 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:01:38 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.030 |  |
| 2026-02-27 10:01:34 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-27 10:01:20 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:00:59 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.052 |  |
| 2026-02-27 10:00:57 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-27 10:00:53 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 10:00:50 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 10:02:04 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-27 10:00:57 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-27 10:03:27 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-27 10:01:34 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-27 10:03:26 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-27 10:04:46 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-27 10:08:32 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-27 10:00:53 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 10:07:29 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-27 10:09:33 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-27 10:07:04 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:02:02 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:01:20 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:02:12 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:01:55 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:16:16 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:08:29 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:03:24 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:04:24 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:03:46 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:03:30 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:02:12 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:03:49 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:05:41 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:06:05 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:08:58 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:07:59 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:06:56 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:16:49 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.008 |  |
| 2026-02-27 10:03:52 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-27 10:02:26 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-27 10:02:09 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-02-27 10:07:27 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.019 |  |
| 2026-02-27 10:00:50 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-02-27 10:01:38 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.030 |  |
| 2026-02-27 10:02:39 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-02-27 10:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.049 |  |
| 2026-02-27 10:00:59 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)