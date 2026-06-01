# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_07:37:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,293 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 07:37:09 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:21:12 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.060 |  |
| 2026-06-01 07:19:35 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:14:44 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:13:23 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-01 07:13:12 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-01 07:12:35 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-01 07:10:09 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:09:26 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.009 |  |
| 2026-06-01 07:08:34 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-06-01 07:07:05 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.019 |  |
| 2026-06-01 07:06:55 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:06:33 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:06:15 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-06-01 07:05:11 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:04:58 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:04:53 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | -0.021 |  |
| 2026-06-01 07:04:38 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.095 |  |
| 2026-06-01 07:04:37 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | -0.039 |  |
| 2026-06-01 07:04:28 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-01 07:04:23 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:04:07 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:03:50 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-06-01 07:03:47 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:03:31 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:03:14 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-06-01 07:03:00 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.029 |  |
| 2026-06-01 07:02:43 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:02:37 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:02:35 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:02:30 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.080 |  |
| 2026-06-01 07:02:12 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-01 07:01:59 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:01:34 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.003 |  |
| 2026-06-01 07:01:28 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:01:12 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:00:39 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.050 |  |
| 2026-06-01 07:00:18 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 07:13:23 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-01 07:04:28 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-01 07:13:12 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-01 07:12:35 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-01 07:01:34 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.003 |  |
| 2026-06-01 07:05:11 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:00:18 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:04:07 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:04:23 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:02:30 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:02:43 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:01:28 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:03:31 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:02:35 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:01:12 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:19:35 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:03:47 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:01:59 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:02:37 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:10:09 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:14:44 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:06:33 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:06:55 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:37:09 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:04:58 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 07:09:26 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.009 |  |
| 2026-06-01 07:06:15 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-06-01 07:03:50 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-06-01 07:02:12 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-01 07:03:14 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-06-01 07:08:34 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-06-01 07:07:05 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.019 |  |
| 2026-06-01 07:04:53 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | -0.021 |  |
| 2026-06-01 07:03:00 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.029 |  |
| 2026-06-01 07:04:37 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | -0.039 |  |
| 2026-06-01 07:00:39 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.050 |  |
| 2026-06-01 07:21:12 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.060 |  |
| 2026-06-01 07:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.080 |  |
| 2026-06-01 07:04:38 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)