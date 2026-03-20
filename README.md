# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_21:13:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,822 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 21:13:19 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-20 21:08:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.039 |  |
| 2026-03-20 21:08:28 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:07:27 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.021 |  |
| 2026-03-20 21:06:39 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.058 |  |
| 2026-03-20 21:06:31 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:06:26 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.052 |  |
| 2026-03-20 21:06:19 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.079 |  |
| 2026-03-20 21:05:45 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.502 |  |
| 2026-03-20 21:05:24 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.095 |  |
| 2026-03-20 21:05:15 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:05:01 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-03-20 21:04:45 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-03-20 21:04:37 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 21:04:33 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:04:30 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:04:29 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.021 |  |
| 2026-03-20 21:04:06 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:03:54 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:03:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:03:31 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:03:24 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:03:16 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.033 |  |
| 2026-03-20 21:03:07 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-20 21:02:53 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:02:49 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:02:35 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-20 21:02:25 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:02:15 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:02:09 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-03-20 21:01:52 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:01:25 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-03-20 21:01:14 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:01:09 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-03-20 21:00:59 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 21:01:09 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-03-20 21:13:19 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-20 21:03:07 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-20 21:00:59 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 18:01:37 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 21:04:37 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 21:01:52 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:08:28 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:03:24 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:02:53 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:58 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:06:31 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:04:06 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:02:15 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:03:31 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:03:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:01:14 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:04:30 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:02:25 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:04:33 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:02:49 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:05:15 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:03:54 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:02:35 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-20 21:05:01 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-03-20 21:02:09 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-03-20 21:04:45 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-03-20 21:01:25 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-03-20 21:04:29 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.021 |  |
| 2026-03-20 21:07:27 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.021 |  |
| 2026-03-20 21:03:16 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.033 |  |
| 2026-03-20 21:08:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.039 |  |
| 2026-03-20 21:06:26 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.052 |  |
| 2026-03-20 21:06:39 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.058 |  |
| 2026-03-20 21:06:19 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.079 |  |
| 2026-03-20 18:01:16 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.091 |  |
| 2026-03-20 21:05:24 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.095 |  |
| 2026-03-20 21:05:45 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.502 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)