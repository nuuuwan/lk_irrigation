# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_09:10:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,088 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 09:10:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:09:25 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.018 |  |
| 2026-06-04 09:07:46 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.035 |  |
| 2026-06-04 09:07:08 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-04 09:07:03 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 09:07:02 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:06:43 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-04 09:06:28 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-04 09:06:12 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 09:05:58 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-04 09:05:39 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:05:20 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 09:05:10 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:04:38 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:04:28 | Rathnapura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.023 |  |
| 2026-06-04 09:04:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:03:51 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 09:03:31 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 09:03:29 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-04 09:03:24 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:03:15 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.023 |  |
| 2026-06-04 09:03:14 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-06-04 09:03:13 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:03:03 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:02:59 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-04 09:02:40 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:02:26 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:02:15 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.031 |  |
| 2026-06-04 09:01:40 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.064 |  |
| 2026-06-04 09:01:30 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-04 09:01:19 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:01:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:01:00 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:00:52 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:00:44 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-06-04 09:00:20 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-06-04 09:00:08 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 09:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-04 09:03:29 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-04 08:05:53 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-04 09:01:30 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-04 09:06:43 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-04 09:06:28 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-04 09:05:58 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-04 09:07:08 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-04 09:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 09:05:20 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 09:03:31 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 09:07:03 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 09:06:12 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 09:02:26 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:01:00 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:00:52 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:03:03 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:01:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:03:51 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:10:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:04:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:05:39 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:04:38 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:03:24 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:01:19 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:02:59 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:02:40 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:07:02 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:05:10 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 09:03:14 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-06-04 09:00:44 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-06-04 09:09:25 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.018 |  |
| 2026-06-04 09:00:20 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-06-04 09:04:28 | Rathnapura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.023 |  |
| 2026-06-04 09:03:15 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.023 |  |
| 2026-06-04 09:02:15 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.031 |  |
| 2026-06-04 09:07:46 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.035 |  |
| 2026-06-04 09:00:08 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.042 |  |
| 2026-06-04 09:01:40 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)