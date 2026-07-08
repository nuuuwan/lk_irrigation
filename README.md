# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_09:10:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **200,498 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 09:10:11 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-07-08 09:09:29 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-07-08 09:08:40 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:07:11 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:07:05 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:07:01 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:06:14 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-07-08 09:05:40 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:05:37 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:05:33 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.042 |  |
| 2026-07-08 09:05:26 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-07-08 09:05:22 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:05:09 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:04:34 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-08 09:04:22 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:04:19 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.038 |  |
| 2026-07-08 09:03:42 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:03:27 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:03:07 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-08 09:03:01 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-07-08 09:03:01 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.050 |  |
| 2026-07-08 09:02:55 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:02:51 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-07-08 09:02:51 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-07-08 09:02:46 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-08 09:02:21 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:02:14 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.335 |  |
| 2026-07-08 09:02:09 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-07-08 09:01:45 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:01:44 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:01:38 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-07-08 09:01:31 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:01:19 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.031 |  |
| 2026-07-08 09:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:01:09 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:00:47 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:00:23 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:00:10 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 09:05:26 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-07-08 09:02:46 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-08 09:04:34 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-08 09:00:47 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:00:23 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:01:44 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:05:22 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:07:01 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:03:42 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:05:09 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:05:40 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:07:11 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:04:22 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:01:45 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:05:37 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:03:01 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:03:27 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:01:31 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:08:40 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:07:05 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:02:21 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:02:55 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:01:09 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 09:10:11 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-07-08 09:02:51 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-07-08 09:03:07 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-08 09:03:01 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-07-08 09:09:29 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-07-08 09:06:14 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-07-08 09:02:51 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-07-08 09:00:10 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-07-08 09:01:38 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-07-08 09:02:09 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-07-08 09:01:19 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.031 |  |
| 2026-07-08 09:04:19 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.038 |  |
| 2026-07-08 09:05:33 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.042 |  |
| 2026-07-08 09:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.050 |  |
| 2026-07-08 09:02:14 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.335 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)