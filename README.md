# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_07:04:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,423 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 07:04:12 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-04-25 07:04:02 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-04-25 07:04:01 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:03:59 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-25 07:03:44 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.021 |  |
| 2026-04-25 07:03:43 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-25 07:03:38 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:03:33 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-04-25 07:03:28 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:03:22 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.080 |  |
| 2026-04-25 07:02:52 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-25 07:02:50 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:02:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-04-25 07:02:46 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:02:29 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-25 07:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.099 |  |
| 2026-04-25 07:01:35 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-04-25 07:01:33 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.059 |  |
| 2026-04-25 07:01:20 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:01:14 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-04-25 07:01:10 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-04-25 07:00:29 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-04-25 07:00:23 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.081 |  |
| 2026-04-25 06:31:46 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-04-25 06:23:20 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.081 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 07:03:59 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-25 06:05:28 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-25 07:03:43 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-25 07:02:29 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-25 07:02:52 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 18:01:26 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 07:03:28 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:02:50 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:01:20 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 06:03:15 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:02:46 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:04:01 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-25 06:09:52 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-04-25 06:04:00 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:03:38 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-25 06:04:15 | Katharagama (Menik Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-25 06:06:09 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-25 07:01:35 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-04-25 06:01:13 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-25 07:01:14 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-04-25 06:03:47 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-04-25 07:01:10 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-04-25 07:04:02 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-04-25 07:03:33 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-04-25 07:03:44 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.021 |  |
| 2026-04-25 06:01:28 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.024 |  |
| 2026-04-25 06:31:46 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-04-25 07:04:12 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-04-25 07:00:29 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-04-25 07:02:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-04-25 06:06:26 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.032 |  |
| 2026-04-25 06:00:14 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.039 |  |
| 2026-04-25 06:05:52 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.040 |  |
| 2026-04-25 06:03:43 | Ellagawa (Kalu Ganga) | 4.76 | 🟢 Normal | -0.048 |  |
| 2026-04-25 07:01:33 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.059 |  |
| 2026-04-25 06:00:50 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.073 |  |
| 2026-04-25 07:03:22 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.080 |  |
| 2026-04-25 07:00:23 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.081 |  |
| 2026-04-25 07:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)