# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_18:11:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,817 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 18:11:16 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:10:46 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.025 |  |
| 2026-06-19 18:09:46 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.027 |  |
| 2026-06-19 18:09:29 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:08:19 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-19 18:07:29 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-06-19 18:05:44 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:05:44 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-19 18:05:34 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:05:27 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.060 |  |
| 2026-06-19 18:05:08 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:05:06 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:04:46 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-06-19 18:04:34 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:04:16 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.030 |  |
| 2026-06-19 18:04:00 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:03:33 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:03:30 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:03:18 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:03:13 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | -0.020 |  |
| 2026-06-19 18:02:55 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-19 18:02:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:43 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:02:42 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:02:38 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-06-19 18:02:33 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:19 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.080 |  |
| 2026-06-19 18:02:18 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-06-19 18:02:16 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.01 | 🟢 Normal | -0.020 |  |
| 2026-06-19 18:02:10 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:01 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-06-19 18:01:58 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:01:42 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.021 |  |
| 2026-06-19 18:01:24 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:01:00 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:00:39 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:00:14 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:00:10 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 18:02:55 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-19 18:08:19 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-19 18:05:44 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-19 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:00:39 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:00:14 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:01:00 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:04:00 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:05:44 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:05:08 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:09:29 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:05:06 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:04:34 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:16 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:03:18 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:00:10 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:05:34 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:11:16 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:01:58 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:10 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:03:33 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:03:30 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:02:42 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:02:43 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:04:46 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-06-19 18:07:29 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-06-19 18:02:01 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-06-19 18:02:38 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-06-19 18:03:13 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | -0.020 |  |
| 2026-06-19 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.01 | 🟢 Normal | -0.020 |  |
| 2026-06-19 18:02:18 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-06-19 18:01:42 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.021 |  |
| 2026-06-19 18:10:46 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.025 |  |
| 2026-06-19 18:09:46 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.027 |  |
| 2026-06-19 18:04:16 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.030 |  |
| 2026-06-19 18:05:27 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.060 |  |
| 2026-06-19 18:02:19 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)