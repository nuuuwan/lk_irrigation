# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_07:24:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,869 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 07:24:20 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:22:06 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:20:26 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-06-24 07:15:58 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.027 |  |
| 2026-06-24 07:13:21 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:12:49 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:09:41 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-24 07:08:42 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-06-24 07:07:48 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:07:10 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.067 |  |
| 2026-06-24 07:07:04 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.019 |  |
| 2026-06-24 07:06:08 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:06:06 | Putupaula (Kalu Ganga) | 2.18 | 🟢 Normal | -0.192 |  |
| 2026-06-24 07:05:37 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:04:52 | Dunamale (Aththanagalu Oya) | 3.18 | 🟢 Normal | -0.067 |  |
| 2026-06-24 07:04:37 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:04:30 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-06-24 07:04:30 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.030 |  |
| 2026-06-24 07:04:23 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:04:18 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | -0.075 |  |
| 2026-06-24 07:03:44 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.040 |  |
| 2026-06-24 07:03:39 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.186 |  |
| 2026-06-24 07:03:35 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:03:25 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-24 07:03:22 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.079 |  |
| 2026-06-24 07:03:21 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-24 07:02:46 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:02:28 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:02:23 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | -0.052 |  |
| 2026-06-24 07:02:15 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | -0.069 |  |
| 2026-06-24 07:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.53 | 🟡 Alert | -0.070 |  |
| 2026-06-24 07:01:55 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.030 |  |
| 2026-06-24 07:01:35 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.002 |  |
| 2026-06-24 07:01:06 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:01:05 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-24 07:00:48 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:00:31 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.031 |  |
| 2026-06-24 07:00:21 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-24 07:00:11 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 07:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.53 | 🟡 Alert | -0.070 |  |
| 2026-06-24 07:03:21 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-24 07:03:25 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-24 07:00:21 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-24 07:01:35 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.002 |  |
| 2026-06-24 07:24:20 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:02:46 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:12:49 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:01:05 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:13:21 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:04:37 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:22:06 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:05:37 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:03:35 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:07:48 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:06:08 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:01:06 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:04:23 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:00:48 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 07:20:26 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-06-24 07:09:41 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-24 07:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-24 07:08:42 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-06-24 07:04:30 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-06-24 07:07:04 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.019 |  |
| 2026-06-24 07:15:58 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.027 |  |
| 2026-06-24 07:04:30 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.030 |  |
| 2026-06-24 07:01:55 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.030 |  |
| 2026-06-24 07:00:31 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.031 |  |
| 2026-06-24 07:00:11 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.031 |  |
| 2026-06-24 07:03:44 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.040 |  |
| 2026-06-24 07:02:23 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | -0.052 |  |
| 2026-06-24 07:04:52 | Dunamale (Aththanagalu Oya) | 3.18 | 🟢 Normal | -0.067 |  |
| 2026-06-24 07:07:10 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.067 |  |
| 2026-06-24 07:02:15 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | -0.069 |  |
| 2026-06-24 07:04:18 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | -0.075 |  |
| 2026-06-24 07:03:22 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.079 |  |
| 2026-06-24 07:03:39 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.186 |  |
| 2026-06-24 07:06:06 | Putupaula (Kalu Ganga) | 2.18 | 🟢 Normal | -0.192 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)