# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_09:17:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **180,783 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 09:17:35 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-16 09:10:33 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-16 09:09:18 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.028 |  |
| 2026-06-16 09:07:52 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.009 |  |
| 2026-06-16 09:07:38 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:07:21 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:07:10 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-16 09:06:52 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-16 09:06:11 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.219 |  |
| 2026-06-16 09:05:44 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-06-16 09:05:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.68 | 🟢 Normal | -0.012 |  |
| 2026-06-16 09:05:13 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-06-16 09:05:06 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-06-16 09:04:52 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | -0.020 |  |
| 2026-06-16 09:04:24 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:03:46 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-06-16 09:03:31 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.023 |  |
| 2026-06-16 09:03:15 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-06-16 09:03:05 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-16 09:03:03 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-16 09:02:54 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:02:53 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:02:31 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.021 |  |
| 2026-06-16 09:02:25 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:02:15 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-16 09:02:12 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:02:03 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-16 09:01:59 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:01:54 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:01:46 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-06-16 09:01:31 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:01:30 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:01:27 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-06-16 09:01:25 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.053 |  |
| 2026-06-16 09:01:18 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:01:11 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-06-16 09:00:42 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-16 09:00:25 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.013 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 09:01:11 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-06-16 09:06:52 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-16 09:07:10 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-16 09:10:33 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-16 09:00:42 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-16 09:02:15 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-16 09:17:35 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-16 09:02:03 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-16 09:00:25 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-16 09:03:05 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-16 09:01:31 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:01:30 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:02:54 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:01:54 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:04:24 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:07:21 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:02:53 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:01:18 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:01:59 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:03:46 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:02:12 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:07:38 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:02:25 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-16 09:07:52 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.009 |  |
| 2026-06-16 09:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-06-16 09:05:13 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-06-16 09:03:03 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-16 09:03:15 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-06-16 09:05:06 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-06-16 09:05:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.68 | 🟢 Normal | -0.012 |  |
| 2026-06-16 09:01:27 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-06-16 09:04:52 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | -0.020 |  |
| 2026-06-16 09:02:31 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.021 |  |
| 2026-06-16 09:03:31 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.023 |  |
| 2026-06-16 09:09:18 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.028 |  |
| 2026-06-16 09:05:44 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-06-16 09:01:46 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-06-16 09:01:25 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.053 |  |
| 2026-06-16 09:06:11 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.219 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)