# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_04:51:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,789 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 04:51:14 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.006 |  |
| 2026-06-05 04:49:28 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:44:08 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-06-05 04:18:40 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-06-05 04:14:58 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.019 |  |
| 2026-06-05 04:12:52 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.074 |  |
| 2026-06-05 04:11:26 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:10:49 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-06-05 04:09:27 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 1.220 | 🔺 Rising |
| 2026-06-05 04:08:28 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | 1.220 | 🔺 Rising |
| 2026-06-05 04:08:12 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | -0.029 |  |
| 2026-06-05 04:08:00 | Rathnapura (Kalu Ganga) | 3.15 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-05 04:06:54 | Ellagawa (Kalu Ganga) | 6.95 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-05 04:06:39 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:06:02 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-05 04:05:26 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-05 04:05:24 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-06-05 04:05:12 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:04:53 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:04:29 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-05 04:04:10 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-05 04:04:05 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:03:49 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:03:26 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:03:24 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-05 04:03:24 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 04:03:24 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:03:22 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-05 04:03:13 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 04:02:40 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-05 04:02:28 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-05 04:01:50 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 04:09:27 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 1.220 | 🔺 Rising |
| 2026-06-05 04:18:40 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-06-05 04:05:24 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-06-05 03:13:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-05 04:04:29 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-05 04:02:28 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-05 04:08:00 | Rathnapura (Kalu Ganga) | 3.15 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-05 03:03:01 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-05 04:06:02 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-05 04:04:10 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-05 04:06:54 | Ellagawa (Kalu Ganga) | 6.95 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-05 04:02:40 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-05 04:03:13 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 04:03:24 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 03:43:15 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-05 04:01:19 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-05 04:03:22 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-05 04:01:50 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 04:05:26 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-05 04:44:08 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-06-05 04:03:24 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-05 04:03:26 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:49:28 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:06:39 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:04:53 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:11:26 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:07:04 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:03:49 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-05 03:03:22 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:01:19 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:05:12 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:04:05 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:03:20 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-05 04:51:14 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.006 |  |
| 2026-06-05 04:10:49 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-06-05 04:14:58 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.019 |  |
| 2026-06-05 04:08:12 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | -0.029 |  |
| 2026-06-05 04:12:52 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)